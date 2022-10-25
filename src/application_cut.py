from typing import Deque, List

import util
from application import Application, ArgumentError


class CutApplication(Application):

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        if len(args) < 2 or len(args) > 3 or args[0] != "-b":
            raise ArgumentError()

        intervals = parse_intervals(args[1])
        lines = util.read_lines(args[2]) if len(args) == 3 else inp

        for line in lines:
            filtered = intervals.filter_included(line)
            out.append(filtered + "\n")

    def help_message(self) -> str:
        return "cut <options> [file]"


class Intervals:

    def __init__(self):
        self.all_before = -1
        self.all_after = float("inf")
        self.indices = set()

    def filter_included(self, line: str) -> str:
        line = line.rstrip()
        included = ""

        for i, char in enumerate(line):
            if self.includes_index(i + 1):
                included += char

        return included

    def includes_index(self, index: int) -> bool:
        return index <= self.all_before \
               or index >= self.all_after \
               or index in self.indices


def parse_intervals(arg: str) -> Intervals:
    intervals = Intervals()

    try:
        for term in arg.split(","):
            if term.startswith("-"):
                all_before = int(term[1:])
                intervals.allBefore = max(intervals.all_before, all_before)
            elif term.endswith("-"):
                all_after = int(term[:-1])
                intervals.all_after = min(intervals.all_after, all_after)
            else:
                split = term.split("-")
                lower, upper = int(split[0]), int(split[1])
                for i in range(lower, upper + 1):
                    intervals.indices.add(i)
    except ValueError:
        raise ArgumentError(f"improperly formatted bytes options '{arg}'")

    return intervals
