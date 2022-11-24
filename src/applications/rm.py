import os
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ApplicationError, ArgumentError


class Rm(Application):
    flag_configuration = FlagConfiguration([
        Flag("-r", bool, "--recursive"),
        Flag("-v", bool, "--verbose"),
        Flag("-f", bool, "--force")
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:

        if not args:
            raise ArgumentError("supply at least one path")

        non_existant_paths = []
        directory_args = []

        for arg in args:
            if os.path.isfile(arg):
                os.remove(arg)
                if self.flags["-v"]:
                    out.append(f"deleted file '{arg}'\n")
            elif os.path.isdir(arg):
                directory_args.append(arg)
                if self.flags["-r"]:
                    os.rmdir(arg)
                    if self.flags["-v"]:
                        out.append(f"deleted directory '{arg}'\n")
            else:
                non_existant_paths.append(arg)

        self._handle_errors(non_existant_paths, directory_args)

    def _handle_errors(
            self, non_existant_paths: List[str], directory_args: List[str]):
        err_msgs = []
        if directory_args and not self.flags["-r"]:
            err_msgs.extend(
                map(
                    lambda arg: f"can not delete directory '{arg}'",
                    directory_args
                )
            )
        if non_existant_paths and not self.flags["-f"]:
            err_msgs.extend(
                map(
                    lambda arg: f"'{arg}' is not a file or directory",
                    non_existant_paths
                )
            )
        if err_msgs:
            raise ApplicationError("\n".join(err_msgs))

    def help_message(self) -> str:
        return "rm [-v -r -f] [directories/files...]"
