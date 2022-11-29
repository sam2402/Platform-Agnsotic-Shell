import re
from collections import deque

import util
from flagging import ApplicationFlagDict, Flag, FlagConfiguration
from .application import Application, ArgumentError, ApplicationError


class Grep(Application):
    """Searches for lines containing a match to the specified pattern

    Flags:
        -v, --invert: inverts match
        -c, --colour: colours the matching sections
    """

    name = "grep"
    flag_configuration = FlagConfiguration([
        Flag("-v", bool, "--invert"),
        Flag("-c", bool)
    ])

    def __init__(
        self,
        flags: ApplicationFlagDict = None,
        highlight_colour: str = "\u001b[35m",  # Magenta
        reset_colour: str = "\u001b[0m"  # White
    ):
        super().__init__(flags)
        self.highlight_colour = highlight_colour
        self.reset_colour = reset_colour

    def run(self, inp: list[str], out: deque[str], args: list[str]):
        if not args:
            raise ArgumentError(type(self), "supply at least one argument")

        try:
            pattern = re.compile(args[0])
        except Exception:
            raise ApplicationError(f"'{args[0]}' is not a valid regex")

        if len(args) > 1:
            files = {
                file_name: util.read_lines(file_name) for file_name in args[1:]
            }
        else:
            files = {"": inp}

        for file_name, lines in files.items():
            for line in lines:

                if self.flags["-v"] ^ (not pattern.search(line)):
                    continue

                if self.flags["-c"]:
                    # Apply colouring to sections which matched the regex
                    line = re.sub(
                        f"({pattern.pattern})",
                        f"{self.highlight_colour}\\g<1>{self.reset_colour}",
                        line
                    )

                if len(files) == 1:
                    out.append(line)
                else:
                    out.append(f"{file_name}:{line}")

    def help_message(self) -> str:
        return "grep [-v -c] <pcre> [files...]"
