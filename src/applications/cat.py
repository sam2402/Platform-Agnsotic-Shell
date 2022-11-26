from typing import Deque, List

import util
from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application


class Cat(Application):
    """Concatenates the content of the given files and prints it to stdout

    Flags:
        -n, --number: numbers all output lines
    """

    flag_configuration = FlagConfiguration([Flag("-n", bool, "--number")])

    def __init__(self, flags: ApplicationFlagDict):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        files = [util.read_lines(file_name) for file_name in args]
        lines = [line for file in files for line in file] if files else inp

        for i, line in enumerate(lines):
            if self.flags["-n"]:
                out.append(f"{i + 1} ")
            out.append(line)

    def help_message(self) -> str:
        return "cat [-n] [files...]"
