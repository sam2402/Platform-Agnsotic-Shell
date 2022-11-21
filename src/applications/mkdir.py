from typing import Deque, List

import os
from .application import Application, ApplicationError


class Mkdir(Application):
    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        already_exists_dir = []
        for arg in args:
            if not os.path.isdir(arg):
                os.mkdir(arg)
            else:
                already_exists_dir.append(arg)
        if already_exists_dir:
            err_msg = "\n".join(
                map(lambda arg: f"directory '{arg}' already exists", already_exists_dir)
            )
            raise ApplicationError(err_msg)

    def help_message(self) -> str:
        return "mkdir [directories...]"
