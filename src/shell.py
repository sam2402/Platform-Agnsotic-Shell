import os
import sys
from collections import deque

import parser
from applications.application import ApplicationError, ArgumentError


def evaluate(cmd_line: str, out: deque[str]):
    out_list = parser.execute_command(cmd_line)
    for term in out_list:
        out.append(term)


class ShellError(Exception):
    """Raised when the shell is used incorrectly"""
    pass


def run_shell():
    """Runs the shell with either a single command or as a REPL

    N.B. the REPL will only be run if this script file is being run directly
    """
    num_args = len(sys.argv) - 1

    if num_args > 0:
        if num_args != 2 or sys.argv[1] != "-c":
            raise ShellError("incorrect usage, try -c '<command>'")
        handle_input(sys.argv[2])
    else:
        while __name__ == "__main__":
            print(os.getcwd() + "> ", end="")
            cmd_line = input()
            handle_input(cmd_line)


def handle_input(cmd_line: str):
    if not cmd_line.strip():
        return

    std_out = deque()
    try:
        evaluate(cmd_line, std_out)
    except ArgumentError as err:
        sys.stderr.write(f"argument error: {err}\n")
    except ApplicationError as err:
        sys.stderr.write(f"application error: {err}\n")
    except parser.ParsingError as err:
        sys.stderr.write(f"parsing error: {err}\n")

    while std_out:
        print(std_out.popleft(), end="")


if __name__ == "__main__":
    run_shell()
