import glob
import re
from typing import List, Tuple

from applications.application import Application, UnsafeApplication
from applications.cat import Cat
from applications.cd import Cd
from applications.cut import Cut
from applications.echo import Echo
from applications.find import Find
from applications.grep import Grep
from applications.head_tail import Head, Tail
from applications.ls import Ls
from applications.pwd import Pwd
from applications.sort import Sort
from applications.uniq import Uniq


# At the moment this just handles semicolons, does
# glob expansion and returns [(application, args)]
def parse_raw_input(raw_line: str) -> List[Tuple[Application, List[str]]]:
    raw_commands = extract_raw_commands(raw_line)
    commands = []

    for raw_command in raw_commands:
        tokens = perform_glob_expansion(raw_command)
        app = app_from_name(tokens[0])
        args = tokens[1:]
        commands.append((app, args))

    return commands


APPLICATIONS = {
    "cat": Cat,
    "cd": Cd,
    "cut": Cut,
    "echo": Echo,
    "find": Find,
    "grep": Grep,
    "head": Head,
    "ls": Ls,
    "pwd": Pwd,
    "sort": Sort,
    "tail": Tail,
    "uniq": Uniq,
}


def app_from_name(app_name: str, try_unsafe=True) -> Application:
    if try_unsafe and app_name.startswith("_"):
        app = app_from_name(app_name[1:], False)
        return UnsafeApplication(app)

    if app_name in APPLICATIONS:
        return APPLICATIONS[app_name]()

    raise ValueError(f"unknown application '{app_name}'")


def extract_raw_commands(raw_line: str) -> List[str]:
    raw_commands = []

    for match in re.finditer("([^\"';]+|\"[^\"]*\"|'[^']*')", raw_line):
        if match.group(0):
            raw_commands.append(match.group(0))

    return raw_commands


def perform_glob_expansion(raw_command: str) -> List[str]:
    tokens = []

    for match in re.finditer("[^\\s\"']+|\"([^\"]*)\"|'([^']*)'", raw_command):
        if match.group(1) or match.group(2):
            quoted = match.group(0)
            tokens.append(quoted[1:-1])
        else:
            globbing = glob.glob(match.group(0))
            if globbing:
                tokens.extend(globbing)
            else:
                tokens.append(match.group(0))

    return tokens



from antlr4 import CommonTokenStream, ParseTreeWalker

from parsing.CommandLexer import CommandLexer
from parsing.CommandParser import CommandParser
from parsing.CommandListener import CommandListener


def parseTreeWalker(input: str):

    lexer = CommandLexer(input)
    tokens = CommonTokenStream(lexer)
    parser = CommandParser(tokens)
    tree = parser.command()



    # listener = newCommandListener()
    # walker = ParseTreeWalker()
    # walker.walk(listener, tree)


class newCommandListener(CommandListener):
    def __init__(self, out_stream, indent='    '):
        self.__out = out_stream
        self.__indent = indent
        self.__indent_level = 0

    def __write(self, s):
        self.__out.write(s)

    def __line(self, s):
        self.__write('\n')
        pfix = self.__indent * self.__indent_level
        self.__write(pfix)
        self.__write(s)

