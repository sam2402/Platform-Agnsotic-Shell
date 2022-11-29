"""
Module for parsing the user input
"""

import glob

from antlr4 import CommonTokenStream, InputStream
from antlr4.tree.Tree import TerminalNodeImpl

from antlr.CommandLexer import CommandLexer
from antlr.CommandParser import CommandParser
from command import Command, SubCommand, PipeCommand, CallCommand


class ParsingError(Exception):
    """Raised when a command is improperly formatted"""
    pass


def execute_command(raw_input: str) -> list[str]:
    """Executes a command from a string and returns the list of outputs

    Args:
        raw_input: the command the user provided to the shell (without \n)

    Returns:
        A list of strings representing the output of the command
    """
    command = parse_command(raw_input)
    return command.execute()


def parse_command(raw_input: str) -> Command:
    """Parses a command string to a Command object

    Args:
        raw_input: the command the user provided to the shell (without \n)

    Returns:
        An instance of the Command class representing the parsed command

    Raises:
        ParsingError if the input does not follow the command grammar
    """
    if not raw_input.strip():
        raise ParsingError("command cannot be empty")

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

    raise AssertionError("sub commands must either be of type PIPE or CALL")


def parse_pipe(ctx: CommandParser.PipeContext) -> PipeCommand:
    call = parse_call(ctx.children[0])

    receiver_node = ctx.children[2]
    if type(receiver_node) == CommandParser.PipeContext:
        receiver = parse_pipe(receiver_node)
    elif type(receiver_node) == CommandParser.CallContext:
        receiver = parse_call(receiver_node)
    else:
        raise AssertionError(
            "receiver from pipe must be a PIPE or CALL command"
        )

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


def parse_redirections(ctxts: list[CommandParser.RedirectionContext]) \
        -> tuple[str | None, str | None]:
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
        else:
            raise AssertionError("invalid redirection symbol")

    return in_file, out_file


def parse_arguments(
        ctxts: list[TerminalNodeImpl | CommandParser.ArgumentContext]) \
        -> list[str]:
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
        elif cur_arg:  # Whitespace, start a new argument
            args.append(cur_arg)
            cur_arg = ""

    if cur_arg:
        args.append(cur_arg)

    return args


def parse_argument(ctx: CommandParser.ArgumentContext) -> list[str]:
    child = ctx.children[0]

    if type(child) == TerminalNodeImpl:
        # Unquoted argument, try glob expansion
        return glob_expand_arg(str(child))

    child = child.children[0]

    # Quoted argument
    if type(child) == CommandParser.SingleQuotedContext:
        return [parse_single_quoted(child)]
    if type(child) == CommandParser.DoubleQuotedContext:
        return [parse_double_quoted(child)]
    if type(child) == CommandParser.BackQuotedContext:
        return parse_back_quoted(child)

    raise AssertionError("invalid argument type")


def glob_expand_arg(arg: str) -> list[str]:
    files = glob.glob(arg)
    return files if files else [arg]


def parse_single_quoted(ctx: CommandParser.SingleQuotedContext) -> str:
    children = ctx.children[1:-1]  # Exclude the opening and closing quote
    quoted = "".join([str(child) for child in children])

    if "\n" in quoted or "'" in quoted:
        raise AssertionError(
            "single quoted sections may not contain single quotes or newlines"
        )

    return quoted


def parse_double_quoted(ctx: CommandParser.DoubleQuotedContext) -> str:
    quoted = ""

    for child in ctx.children[1:-1]:
        if type(child) == TerminalNodeImpl:  # Terminal node is UNQUOTED
            if "\"" in str(child) or "\n" in str(child):
                raise AssertionError(
                    "double quoted sections may not "
                    "contain double quotes or newlines"
                )
            quoted += str(child)
        else:
            assert type(child) == CommandParser.BackQuotedContext
            # Expanded backquoted commands
            quoted += " ".join(parse_back_quoted(child))

    return quoted


def parse_back_quoted(ctx: CommandParser.BackQuotedContext) -> list[str]:
    children = ctx.children[1:-1]  # Exclude the opening and closing backtick
    raw_command = "".join([str(child) for child in children])

    if "`" in raw_command or "\n" in raw_command:
        raise AssertionError(
            "back quoted section may not contain back quotes or newlines"
        )

    output = execute_command(raw_command)
    return [s.strip() for s in output]
