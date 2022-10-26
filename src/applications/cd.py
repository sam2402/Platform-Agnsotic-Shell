import os
from typing import Deque, List

from ..application import Application, ArgumentError


class Cd(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]):
        if len(args) != 1:
            raise ArgumentError()

        os.chdir(args[0])

    def help_message(self) -> str:
        return "cd <directory>"
