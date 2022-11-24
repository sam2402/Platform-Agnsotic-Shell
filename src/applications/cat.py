from typing import Deque, Dict, List, Union

from . import util
from .application import Application


class Cat(Application):

    def __init__(self, flags: Dict[str, Union[str, int, bool]]):
        super().__init__(flags)

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
