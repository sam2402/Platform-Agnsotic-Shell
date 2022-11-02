from typing import Deque, List

from . import util
from .application import Application


class Uniq(Application):

    def _run(self, inp: List[str], out: Deque[str], args: List[str]) -> None:
        ignore_case, file_name = util.parse_opt_boolean_flag(args, "-i")
        lines = util.read_lines(file_name) if file_name else inp

        last = None

        for line in lines:
            if line == last or \
               (ignore_case and last and line.lower() == last.lower()):
                continue

            out.append(line)
            last = line

    def help_message(self) -> str:
        return "uniq [-i] [file]"
