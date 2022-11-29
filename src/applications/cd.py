import os
from collections import deque

from flagging import ApplicationFlagDict
from .application import Application, ApplicationError, ArgumentError


class Cd(Application):
    """Changes the current working directory"""

    name = "cd"

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: list[str], out: deque[str], args: list[str]):
        if len(args) != 1:
            raise ArgumentError(type(self), "missing path argument")

        try:
            os.chdir(args[0])
        except FileNotFoundError:
            raise ApplicationError(f"no such directory '{args[0]}'")
        except NotADirectoryError:
            raise ApplicationError(f"'{args[0]}' is not a directory")

    def help_message(self) -> str:
        return "cd <directory>"
