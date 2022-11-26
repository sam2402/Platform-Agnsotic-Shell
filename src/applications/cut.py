from typing import Deque, List

import util
from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ArgumentError, ApplicationError


class Cut(Application):
    """Cuts out sections from each line of a given file or stdin

    The removed sections are outputted to stdout

    Flags:
        -b <interval>: required - specifies the bytes to extract from each line
    """

    name = "cut"
    flag_configuration = FlagConfiguration([Flag("-b", str, argument_count=1)])

    def __init__(self, flags: ApplicationFlagDict = None):
        super().__init__(flags)

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        if len(args) not in [0, 1]:
            raise ArgumentError(type(self), "supply at most one file path")

        intervals = parse_intervals(self.flags["-b"])
        lines = util.read_lines(args[0]) if len(args) == 1 else inp

        for line in lines:
            filtered = intervals.filter_included(line)
            out.append(filtered + "\n")

    def help_message(self) -> str:
        return "cut -b <intervals> [file]"


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
        return (
            index <= self.all_before or
            index >= self.all_after or
            index in self.indices
        )


def parse_intervals(arg: str) -> Intervals:
    intervals = Intervals()

    try:
        for term in arg.split(","):
            if term.startswith("-"):
                all_before = int(term[1:])
                intervals.all_before = max(intervals.all_before, all_before)
            elif term.endswith("-"):
                all_after = int(term[:-1])
                intervals.all_after = min(intervals.all_after, all_after)
            elif "-" in term:
                split = term.split("-")
                lower, upper = int(split[0]), int(split[1])
                for i in range(lower, upper + 1):
                    intervals.indices.add(i)
            else:
                intervals.indices.add(int(term))
    except ValueError:
        raise ApplicationError(f"improperly formatted bytes options '{arg}'")

    return intervals
