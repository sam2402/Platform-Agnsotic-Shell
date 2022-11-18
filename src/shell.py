import os
import sys
from collections import deque
from typing import Deque

import parser
from applications.application import ApplicationError, ArgumentError


def evaluate(cmd_line: str, out: Deque[str]):
    out_list = parser.execute_command(cmd_line)
    for term in out_list:
        out.append(term)


# Raised when the shell is used incorrectly
class ShellError(Exception):
    pass


def run_shell():
    num_args = len(sys.argv) - 1

    if num_args > 0:
        if num_args != 2 or sys.argv[1] != "-c":
            raise ShellError("incorrect usage, try -c '<command>'")
        handle_input(sys.argv[2])
    else:
        while True:
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
        print("wrong arguments, try:", err)
    except ApplicationError as err:
        print("application error:", err)
    except parser.ParsingError as err:
        print("parsing error:", err)

    while std_out:
        print(std_out.popleft(), end="")


if __name__ == "__main__":
    run_shell()
