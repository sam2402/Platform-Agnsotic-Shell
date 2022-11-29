import random
from collections import deque

import util
from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application


class Sort(Application):
    """Sorts the contents of a file/stdin line by line

    Prints the result to stdout.

    Flags:
        -r: sorts in reverse order
        -R: randomises order
    """

    name = "sort"
    flag_configuration = FlagConfiguration([
        Flag("-r", bool, "--reverse"),
        Flag("-R", bool, "--random")
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: list[str], out: deque[str], args: list[str]) -> None:
        lines = util.read_lines(args[0]) if len(args) == 1 else inp

        if self.flags["-R"]:
            random.shuffle(lines)
        else:
            lines = sorted(lines, reverse=self.flags["-r"])

        for line in lines:
            out.append(line)

    def help_message(self) -> str:
        return "sort [-r -R] [file]"
