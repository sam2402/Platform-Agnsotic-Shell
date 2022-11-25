import random
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from . import util
from .application import Application


class Sort(Application):
    flag_configuration = FlagConfiguration([
        Flag("-r", bool, "--reverse"),
        Flag("-R", bool, "--random")
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        lines = util.read_lines(args[0]) if len(args) == 1 else inp

        if self.flags["-R"]:
            random.shuffle(lines)
        else:
            lines = sorted(lines, reverse=self.flags["-r"])

        for line in lines:
            out.append(line)

    def help_message(self) -> str:
        return "sort [-r -R] [file]"
