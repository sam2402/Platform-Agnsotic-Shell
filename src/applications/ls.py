import os
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ApplicationError


class Ls(Application):
    """Lists the content of a directory

    It prints a list of files and directories separated by tabs and followed
    by a newline

    Flags:
        -a:             lists all files including hidden file starting with '.'
        -r, --reverse:  lists in reverse order
        -s, --size:     lists file size
    """

    name = "ls"
    flag_configuration = FlagConfiguration([
        Flag("-a", bool),
        Flag("-r", bool, "--reverse"),
        Flag("-s", bool, "--size")
    ])

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
        if self.flags["-r"]:
            files = files[::-1]
        if self.flags["-s"]:
            files = [
                f"{(os.stat(file).st_size if os.path.isfile(file) else 0)} "
                f"{file}"
                for file in files
            ]

        if len(files):
            out.append("\t".join(files) + "\n")

    def help_message(self) -> str:
        return "ls [-a -r -s] [directory]"
