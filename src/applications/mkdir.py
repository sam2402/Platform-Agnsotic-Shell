import os
from collections import deque

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ApplicationError


class Mkdir(Application):
    """Create a new directory

    Flags:
        -v, --verbose:  displays a message for every directory created
        -p:             enables the creation of parent directories as necessary
    """

    name = "mkdir"
    flag_configuration = FlagConfiguration([
        Flag("-v", bool, "--verbose"),
        Flag("-p", bool)
    ])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: list[str], out: deque[str], args: list[str]) -> None:
        already_exists_dir = []
        non_existent_parent_dirs = []
        make_directory = os.makedirs if self.flags["-p"] else os.mkdir

        for arg in args:
            if not os.path.isdir(arg):
                try:
                    make_directory(arg)
                    if self.flags["-v"]:
                        out.append(f"created directory {arg}\n")
                except FileNotFoundError:
                    non_existent_parent_dirs.append(arg)
            else:
                already_exists_dir.append(arg)

        self._handle_errors(already_exists_dir, non_existent_parent_dirs)

    def _handle_errors(
            self,
            already_exists_dir: list[str],
            non_existent_parent_dirs: list[str]):
        err_msgs = []
        if already_exists_dir:
            err_msgs.extend(
                map(
                    lambda arg: f"directory '{arg}' already exists",
                    already_exists_dir
                )
            )
        if non_existent_parent_dirs:
            err_msgs.extend(
                map(
                    lambda arg: f"path does not exist to '{arg}'",
                    non_existent_parent_dirs
                )
            )

        if err_msgs:
            raise ApplicationError("\n".join(err_msgs))

    def help_message(self) -> str:
        return "mkdir [-v -p] [directories...]"
