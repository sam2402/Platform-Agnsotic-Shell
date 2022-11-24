import os
from typing import Deque, List

from flagging import ApplicationFlagDict
from .application import Application


class Pwd(Application):
    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        out.append(os.getcwd() + "\n")

    def help_message(self) -> str:
        return "pwd"
