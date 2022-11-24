from typing import Deque, List

from flagging import Flag, FlagConfiguration

from . import util
from .application import Application


class Uniq(Application):

    flag_configuration = FlagConfiguration([
        Flag("-i", bool, "--ignore-case")
    ])

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        lines = util.read_lines(args[0]) if len(args) == 1 else inp

        last = None

        for line in lines:
            if line == last or \
               (self.flags["-i"] and last and line.lower() == last.lower()):
                continue

            out.append(line)
            last = line

    def help_message(self) -> str:
        return "uniq [-i] [file]"
