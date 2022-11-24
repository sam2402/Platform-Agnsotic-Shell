import glob
from typing import List, Optional, Tuple, Union

from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Tree import TerminalNodeImpl

from antlr.CommandLexer import CommandLexer
from antlr.CommandParser import CommandParser
from command import Command, SubCommand, PipeCommand, CallCommand


# Raised when a command is improperly formatted
class ParsingError(Exception):
    pass


def execute_command(raw_input: str) -> List[str]:
    command = parse_command(raw_input)
    return command.execute()


def parse_command(raw_input: str) -> Command:
    lexer = CommandLexer(InputStream(raw_input))
    tokens = CommonTokenStream(lexer)
    parser = CommandParser(tokens)

    # Silence ANTLR error output in favour of ours
    lexer.removeErrorListeners()
    parser.removeErrorListeners()

    tree = parser.command()
    return command_from_tree(tree)


def command_from_tree(ctx: CommandParser.CommandContext) -> Command:
    sub_commands = [parse_sub_command(child)
                    for child in ctx.children
                    if type(child) == CommandParser.SubCommandContext]
    return Command(sub_commands)


def parse_sub_command(ctx: CommandParser.SubCommandContext) -> SubCommand:
    if len(ctx.children) != 1:
        raise ParsingError("improperly formatted subcommand")
    child = ctx.children[0]

    if type(child) == CommandParser.PipeContext:
        return parse_pipe(child)
    if type(child) == CommandParser.CallContext:
        return parse_call(child)

    raise ParsingError("sub commands must either be of type PIPE or CALL")


def parse_pipe(ctx: CommandParser.PipeContext) -> PipeCommand:
    if len(ctx.children) != 3:
        raise ParsingError("improperly formatted pipe command")
    if type(ctx.children[0]) != CommandParser.CallContext:
        raise ParsingError("input to pipe must be a CALL command")

    call = parse_call(ctx.children[0])

    receiver_node = ctx.children[2]
    if type(receiver_node) == CommandParser.PipeContext:
        receiver = parse_pipe(receiver_node)
    elif type(receiver_node) == CommandParser.CallContext:
        receiver = parse_call(receiver_node)
    else:
        raise ParsingError("receiver from pipe must be a PIPE or CALL command")

    return PipeCommand(call, receiver)


def parse_call(ctx: CommandParser.CallContext) -> CallCommand:
    redirections = list(filter(
        lambda c: type(c) == CommandParser.RedirectionContext,
        ctx.children
    ))

    in_file, out_file = parse_redirections(redirections)
    args = parse_arguments(ctx.children)

    return CallCommand(args, in_file, out_file)


IN = "<"
OUT = ">"


def parse_redirections(ctxts: List[CommandParser.RedirectionContext]) \
        -> Tuple[Optional[str], Optional[str]]:
    in_file = None
    out_file = None

    for ctx in ctxts:
        redirect_type = str(ctx.children[0])
        file = parse_argument(ctx.children[1 if len(ctx.children) == 2 else 2])
        file = file[0]

        if redirect_type == IN:
            if in_file:
                raise ParsingError("more than one input file specified")
            in_file = file
        elif redirect_type == OUT:
            if out_file:
                raise ParsingError("more than one output file specified")
            out_file = file

    return in_file, out_file


def parse_arguments(
        ctxts: List[Union[TerminalNodeImpl, CommandParser.ArgumentContext]])\
        -> List[str]:
    args = []
    cur_arg = ""

    # Combines arguments if there is no whitespace between them
    # e.g. a"b"c -> abc
    for child in ctxts:
        if type(child) == CommandParser.ArgumentContext:
            arg = parse_argument(child)
            if len(arg) == 1:
                cur_arg += arg[0]
            else:
                args.extend(arg)
                cur_arg = ""
        elif cur_arg:  # Whitespace
            args.append(cur_arg)
            cur_arg = ""

    if cur_arg:
        args.append(cur_arg)

    return args


def parse_argument(ctx: CommandParser.ArgumentContext) -> List[str]:
    child = ctx.children[0]

    if type(child) == TerminalNodeImpl:
        # Unquoted argument
        return glob_expand_arg(str(child))

    child = child.children[0]

    # Quoted argument
    if type(child) == CommandParser.SingleQuotedContext:
        return [parse_single_quoted(child)]
    if type(child) == CommandParser.DoubleQuotedContext:
        return [parse_double_quoted(child)]
    if type(child) == CommandParser.BackQuotedContext:
        return parse_back_quoted(child)

    raise ParsingError("unknown argument type")


def glob_expand_arg(arg: str) -> List[str]:
    files = glob.glob(arg)
    return files if files else [arg]


def parse_single_quoted(ctx: CommandParser.SingleQuotedContext) -> str:
    quoted = "".join([str(child) for child in ctx.children[1:-1]])

    if "\n" in quoted or "'" in quoted:
        raise ParsingError(
            "single quoted sections may not contain single quotes or newlines"
        )

    return quoted


def parse_double_quoted(ctx: CommandParser.DoubleQuotedContext) -> str:
    quoted = ""

    for child in ctx.children[1:-1]:
        if type(child) == TerminalNodeImpl:
            if "\"" in str(child) or "\n" in str(child):
                raise ParsingError(
                    "double quoted sections may not "
                    "contain double quotes or newlines"
                )
            quoted += str(child)
        elif type(child) == CommandParser.BackQuotedContext:
            quoted += " ".join(parse_back_quoted(child))

    return quoted


def parse_back_quoted(ctx: CommandParser.BackQuotedContext) -> List[str]:
    raw_command = "".join([str(child) for child in ctx.children[1:-1]])

    if "`" in raw_command or "\n" in raw_command:
        raise ParsingError(
            "back quoted section may not contain back quotes or newlines"
        )

    return [s.strip() for s in execute_command(raw_command)]
