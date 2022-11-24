import os
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ApplicationError


class Ls(Application):
    flag_configuration = FlagConfiguration([Flag("-a", bool)])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        directory = os.getcwd() if len(args) == 0 else args[0]

        try:
            files = os.listdir(directory)
        except FileNotFoundError:
            raise ApplicationError(f"no such directory '{directory}'")

        if not self.flags["-a"]:
            files = list(filter(lambda file: not file.startswith("."), files))

        if len(files):
            out.append("\t".join(files) + "\n")

    def help_message(self) -> str:
        return "ls [-a] [directory]"
