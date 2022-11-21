from typing import Deque, List

from . import util
from .application import Application


class Cat(Application):

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        if not args:
            for line in inp:
                out.append(line)
        else:
            for file_name in args:
                for line in util.read_lines(file_name):
                    out.append(line)

    def help_message(self) -> str:
        return "cat [files...]"
