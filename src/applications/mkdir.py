import os
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ApplicationError


class Mkdir(Application):
    flag_configuration = FlagConfiguration([Flag("-v", bool, "--verbose")])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        already_exists_dir = []
        for arg in args:
            if not os.path.isdir(arg):
                os.mkdir(arg)
                if self.flags["-v"]:
                    out.append(f"created directory {arg}\n")
            else:
                already_exists_dir.append(arg)
        if already_exists_dir:
            err_msg = "\n".join(
                map(
                    lambda arg: f"directory '{arg}' already exists",
                    already_exists_dir
                )
            )
            raise ApplicationError(err_msg)

    def help_message(self) -> str:
        return "mkdir [-v] [directories...]"
