from abc import ABC
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from . import util
from .application import Application, ArgumentError


class FileLineOutputter(Application, ABC):
    flag_configuration = FlagConfiguration([
        Flag("-n", int, default_value=10, argument_count=1, is_optional=True),
        Flag("-v", bool, "--verbose")
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self,
            inp: List[str],
            out: Deque[str],
            args: List[str], invert: bool = False
            ):
        if len(args) > 1:
            raise ArgumentError("supply at most one file path")

        lines = self._get_lines(
            inp,
            args,
            self.flags["-n"] if not invert else -self.flags["-n"]
        )
        if self.flags["-v"]:
            out.append(f"==>{args[0]}<==\n")
        out.append("".join(lines))

    def _get_lines(self, inp: List[str], args: List[str], max_line_count: int):
        lines = util.read_lines(args[0]) if len(args) == 1 else inp
        line_count = max_line_count if abs(max_line_count) < len(lines) \
            else len(lines)
        return lines[:line_count] if line_count >= 0 else lines[line_count:]


class Head(FileLineOutputter):
    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        super().run(inp, out, args)

    def help_message(self) -> str:
        return "head [-v -n lines] [file]"


class Tail(FileLineOutputter):
    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        super().run(inp, out, args, invert=True)

    def help_message(self) -> str:
        return "tail [-v -n lines] [file]"
