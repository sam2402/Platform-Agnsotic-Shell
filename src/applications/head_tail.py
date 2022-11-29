from abc import ABC
from collections import deque

import util
from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ArgumentError


class FileLineOutputter(Application, ABC):
    """Abstract class to handle common implementation
    details of head and tail"""
    flag_configuration = FlagConfiguration([
        Flag("-n", int, default_value=10, argument_count=1, is_optional=True),
        Flag("-v", bool, "--verbose")
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self,
            inp: list[str],
            out: deque[str],
            args: list[str], invert: bool = False
            ):
        if len(args) > 1:
            raise ArgumentError(type(self), "supply at most one file path")

        lines = self._get_lines(
            inp,
            args,
            self.flags["-n"] if not invert else -self.flags["-n"]
        )
        if self.flags["-v"]:
            out.append(f"==>{args[0]}<==\n")
        out.extend(lines)

    def _get_lines(self, inp: list[str], args: list[str], max_line_count: int):
        lines = util.read_lines(args[0]) if len(args) == 1 else inp
        line_count = max_line_count if abs(max_line_count) < len(lines) \
            else len(lines)
        return lines[:line_count] if line_count >= 0 else lines[line_count:]


class Head(FileLineOutputter):
    """Prints the first N lines of a given file or stdin

    If there are less than N lines, prints only the existing lines without
    raising an exception.

    Flags:
        -n <number of line: int>:   Specifies the number of lines to output
        -v, --verbose:              Precedes data from file with file name
    """

    name = "head"

    def run(self, inp: list[str], out: deque[str], args: list[str]):
        super().run(inp, out, args, invert=False)

    def help_message(self) -> str:
        return "head [-v -n lines] [file]"


class Tail(FileLineOutputter):
    """Prints the last N lines of a given file or stdin. If there are less
    than N lines, prints only the existing lines without raising an exception.

    Flags:
        -n <number of line: int>:   Specifies the number of lines to output
        -v, --verbose:              Precede data from file with file name
    """

    name = "tail"

    def run(self, inp: list[str], out: deque[str], args: list[str]):
        super().run(inp, out, args, invert=True)

    def help_message(self) -> str:
        return "tail [-v -n lines] [file]"
