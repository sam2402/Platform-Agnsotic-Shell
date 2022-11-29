import os
from collections import deque

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application


class Pwd(Application):
    """Output the path of the working directory to std out

    Starting from the root

    Flags:
        -P: prints the path with symbolic links resolved
    """

    name = "pwd"
    flag_configuration = FlagConfiguration([
        Flag("-P", bool),
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: list[str], out: deque[str], args: list[str]) -> None:
        cwd = os.getcwd()
        if self.flags["-P"]:
            cwd = os.path.realpath(cwd)
        out.append(cwd + "\n")

    def help_message(self) -> str:
        return "pwd [-P]"
