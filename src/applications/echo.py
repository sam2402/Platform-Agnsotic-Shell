from typing import Deque, List

from ..application import Application


class Echo(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        output = " ".join(args) + "\n"
        out.append(output)

    def help_message(self) -> str:
        return "echo [args...]"
