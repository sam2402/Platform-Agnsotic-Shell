import os
import shutil
from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ApplicationError, ArgumentError


class Rm(Application):
    """Deletes files

    Flags:
        -r/--recursive: removes directories and their contents recursively
        -v/--verbose:   outputs a message for each deletion
        -f/--force:     enables the deletion of non empty directories and
                        ignore non-existent paths
    """

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

        non_existent_paths = []
        directory_args = []
        non_empty_directories = []

        delete_directory = shutil.rmtree if self.flags["-f"] else os.rmdir

        for arg in args:
            if os.path.isfile(arg):
                os.remove(arg)
                if self.flags["-v"]:
                    out.append(f"deleted file '{arg}'\n")
            elif os.path.isdir(arg):
                directory_args.append(arg)
                if self.flags["-r"]:
                    try:
                        delete_directory(arg)
                        if self.flags["-v"]:
                            out.append(f"deleted directory '{arg}'\n")
                    except OSError:
                        non_empty_directories.append(arg)
            else:
                non_existent_paths.append(arg)

        self._handle_errors(
            non_existent_paths,
            directory_args,
            non_empty_directories
        )

    def _handle_errors(
            self,
            non_existent_paths: List[str],
            directory_args: List[str],
            non_empty_directories: List[str]):
        err_msgs = []
        if directory_args and not self.flags["-r"]:
            err_msgs.extend(
                map(
                    lambda arg: f"can not delete directory '{arg}'",
                    directory_args
                )
            )
        if non_existent_paths and not self.flags["-f"]:
            err_msgs.extend(
                map(
                    lambda arg: f"'{arg}' is not a file or directory",
                    non_existent_paths
                )
            )
        if non_empty_directories and not self.flags["-f"]:
            err_msgs.extend(
                map(
                    lambda arg: f"'{arg}' is not an empty directory",
                    non_empty_directories
                )
            )
        if err_msgs:
            raise ApplicationError("\n".join(err_msgs))

    def help_message(self) -> str:
        return "rm [-v -r -f] [directories/files...]"
