from abc import ABC
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from . import util
from .application import Application


class FileLineOutputter(Application, ABC):
    flag_configuration = FlagConfiguration(
        [Flag("-n", int, default_value=10, argument_count=1, is_optional=True)]
    )

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def get_lines(self, inp: List[str], args: List[str], max_line_count: int):
        lines = util.read_lines(args[0]) if len(args) == 1 else inp
        line_count = max_line_count if abs(max_line_count) < len(lines) \
            else len(lines)
        return lines[:line_count] if line_count >= 0 else lines[line_count:]


class Head(FileLineOutputter):
    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        out.append("".join(self.get_lines(inp, args, self.flags["-n"])))

    def help_message(self) -> str:
        return "head [-n lines] [file]"


class Tail(FileLineOutputter):
    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        out.append("".join(self.get_lines(inp, args, -self.flags["-n"])))

    def help_message(self) -> str:
        return "tail [-n lines] [file]"
