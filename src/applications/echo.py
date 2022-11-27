from typing import Deque, List

from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application


class Echo(Application):
    """Prints its arguments to stdout

    The arguments are separated by spaces and followed by a newline

    Flags:
        -n: omits trailing newline
    """

    name = "echo"
    flag_configuration = FlagConfiguration([Flag("-n", bool)])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        output = " ".join(args)
        output += "\n" if not self.flags["-n"] else ""
        out.append(output)

    def help_message(self) -> str:
        return "echo [-n] [args...]"
