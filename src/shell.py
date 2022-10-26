import os
import sys
from collections import deque
from typing import Deque

import parser


def evaluate(cmd_line: str, out: Deque[str]):
    for app, args in parser.parse_raw_input(cmd_line):
        app.execute([], out, args)


def run_shell():
    num_args = len(sys.argv) - 1

    if num_args > 0:
        if num_args != 2 or sys.argv[1] != "-c":
            raise ValueError("incorrect usage, try -c '<command>'")
        handle_input(sys.argv[2])
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmd_line = input()
            handle_input(cmd_line)


def handle_input(cmd_line: str):
    std_out = deque()
    evaluate(cmd_line, std_out)

    while std_out:
        print(std_out.popleft(), end="")


if __name__ == "__main__":
    run_shell()
