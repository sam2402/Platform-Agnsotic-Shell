from typing import Deque, Dict, List, Union

from .application import Application


class Echo(Application):

    def __init__(self, flags: Dict[str, Union[str, int, bool]] = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        output = " ".join(args) + "\n"
        out.append(output)

    def help_message(self) -> str:
        return "echo [args...]"
