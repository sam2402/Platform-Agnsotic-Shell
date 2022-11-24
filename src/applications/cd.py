import os
from typing import Deque, Dict, List, Union

from .application import Application, ApplicationError, ArgumentError


class Cd(Application):

    def __init__(self, flags: Dict[str, Union[str, int, bool]] = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        if len(args) != 1:
            raise ArgumentError()

        try:
            os.chdir(args[0])
        except FileNotFoundError:
            raise ApplicationError(f"no such directory '{args[0]}'")
        except NotADirectoryError:
            raise ApplicationError(f"'{args[0]}' is not a directory")

    def help_message(self) -> str:
        return "cd <directory>"
