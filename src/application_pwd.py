import os
from typing import Deque, List

from application import Application


class PwdApplication(Application):

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        out.append(os.getcwd() + "\n")

    def help_message(self) -> str:
        return "pwd"
