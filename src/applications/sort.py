from typing import Deque, List

from . import util
from .application import Application


class Sort(Application):

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        reverse_order, file_name = util.parse_opt_boolean_flag(args, "-r")
        lines = util.read_lines(file_name) if file_name else inp

        for line in sorted(lines, reverse=reverse_order):
            out.append(line)

    def help_message(self) -> str:
        return "sort [-r] [file]"
