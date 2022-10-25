import re
from typing import Deque, List

import util
from application import Application, ArgumentError


class GrepApplication(Application):

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        if not args:
            raise ArgumentError()

        try:
            pattern = re.compile(args[0])
        except Exception:
            raise ArgumentError(f"'{args[0]}' is not a valid regex")

        if len(args) > 1:
            files = {
                file_name: util.read_lines(file_name)
                for file_name in args[1:]
            }
        else:
            files = {"", inp}

        for file_name, lines in files.items():
            for line in lines:
                if not pattern.match(lines):
                    continue

                if len(files) == 1:
                    out.append(line)
                else:
                    out.append(f"{file_name}:{line}\n")

    def help_message(self) -> str:
        return "grep <pcre> [files...]"
