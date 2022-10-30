import os
from typing import Deque, List

from . import util
from .application import Application


class Ls(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        show_hidden, directory = util.parse_opt_boolean_flag(args, "-a")
        if not directory:
            directory = os.getcwd()

        files = os.listdir(directory)
        if not show_hidden:
            files = list(filter(lambda file: not file.startswith("."), files))

        out.append("\t".join(files) + "\n")

    def help_message(self) -> str:
        return "ls [-a] [directory]"
