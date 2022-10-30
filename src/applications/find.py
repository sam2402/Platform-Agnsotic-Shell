import fnmatch
import os
from typing import Deque, List

from .application import Application, ArgumentError


class Find(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]):
        if len(args) not in [2, 3]:
            raise ArgumentError()
        if args[0 if len(args) == 2 else 1] != "-name":
            raise ArgumentError()

        path = args[0] if len(args) == 3 else "."
        pattern = args[1] if len(args) == 2 else args[2]

        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    out.append(os.path.join(root, name) + "\n")

    def help_message(self) -> str:
        return "find [path] -name <pattern>"
