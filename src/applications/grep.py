import re
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from . import util
from .application import Application, ArgumentError, ApplicationError


class Grep(Application):

    flag_configuration = FlagConfiguration([Flag("-v", bool, "--invert")])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        if not args:
            raise ArgumentError()

        try:
            pattern = re.compile(args[0])
        except Exception:
            raise ApplicationError(f"'{args[0]}' is not a valid regex")

        if len(args) > 1:
            files = {
                file_name: util.read_lines(file_name) for file_name in args[1:]
            }
        else:
            files = {"": inp}

        for file_name, lines in files.items():
            for line in lines:

                if self.flags["-v"] ^ (not pattern.search(line)):
                    continue

                if len(files) == 1:
                    out.append(line)
                else:
                    out.append(f"{file_name}:{line}")

    def help_message(self) -> str:
        return "grep [-v] <pcre> [files...]"
