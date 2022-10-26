from typing import Deque, List

from .. import util
from ..application import Application


class Head(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]):
        execute(inp, out, args, False)

    def help_message(self) -> str:
        return "head [-n lines] [file]"


class Tail(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]):
        execute(inp, out, args, True)

    def help_message(self) -> str:
        return "tail [-n lines] [file]"


def execute(inp: List[str], out: Deque[str], args: List[str], tail: bool):
    no_lines, file_name = util.parse_opt_int_flag(args, "-n", 10)
    lines = util.read_lines(file_name) if file_name else inp

    if tail:
        lines = lines[::-1]

    for i in range(min(no_lines, len(lines))):
        out.append(lines[i])
