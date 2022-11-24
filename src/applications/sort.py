from typing import Deque, Dict, List, Union

from flagging import Flag, FlagConfiguration

from . import util
from .application import Application


class Sort(Application):

    flag_configuration = FlagConfiguration([
        Flag("-r", bool, "--reverse")
    ])

    def __init__(self, flags: Dict[str, Union[str, int, bool]] = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:

        lines = util.read_lines(args[0]) if len(args) == 1 else inp

        for line in sorted(lines, reverse=self.flags["-r"]):
            out.append(line)

    def help_message(self) -> str:
        return "sort [-r] [file]"
