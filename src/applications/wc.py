import os
from typing import Deque, List

import util
from flagging import ApplicationFlagDict, Flag, FlagConfiguration

from .application import Application, ApplicationError


class Wc(Application):
    """Prints the word, line and byte count for a file

    It prints a list of files and directories separated by tabs and followed
    by a newline

    Flags:
        -w:  prints the total number of words
        -l:  prints the total number of lines
        -b:  prints the total number of bytes
    """

    name = "wc"
    flag_configuration = FlagConfiguration([
        Flag("-w", bool),
        Flag("-l", bool),
        Flag("-b", bool)
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:

        total = 0
        if len(inp) > 0:
            total = len(inp)

        for file_name in args:
            if not os.path.isfile(file_name):
                raise ApplicationError(f"no such file '{file_name}'")
            else:
                if self.flags["-b"]:
                    total += os.stat(file_name).st_size
                if self.flags["-w"]:
                    lines = util.read_lines(file_name)
                    total += len(lines)
                if self.flags["-l"]:
                    with open(file_name, 'r') as fp:
                        total += len(fp.readlines())

        out.append(str(total) + "\n")

    def help_message(self) -> str:
        return "wc [-w -l -b] [files...]"
