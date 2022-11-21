import os
from abc import ABC, abstractmethod
from collections import deque
from typing import List

import parser
from applications.application import ApplicationError


class SubCommand(ABC):

    @abstractmethod
    def execute(self, inp: List[str]) -> List[str]:
        pass


class CallCommand(SubCommand):

    def __init__(self, args: List[str], in_file: str, out_file: str):
        self.args = args
        self.in_file = in_file
        self.out_file = out_file

    def execute(self, inp: List[str]) -> List[str]:
        if self.in_file and not inp:
            if not os.path.exists(self.in_file):
                raise ApplicationError(
                    f"input file '{self.in_file} does not exist"
                )
            inp = read_lines(self.in_file)

        application = parser.app_from_name(self.args[0])
        out = deque()
        application.run(inp, out, self.args[1:])

        if self.out_file:
            write_lines(self.out_file, list(out))
            return []

        return list(out)


class PipeCommand(SubCommand):

    def __init__(self, call: CallCommand, receiver: SubCommand):
        self.call = call
        self.receiver = receiver

    def execute(self, inp: List[str]) -> List[str]:
        out = self.call.execute(inp)
        return self.receiver.execute(out)


class Command:

    def __init__(self, sub_commands: List[SubCommand]):
        self.sub_commands = sub_commands

    def execute(self) -> List[str]:
        out = [line
               for sub_command in self.sub_commands
               for line in sub_command.execute([])]
        return out


def read_lines(file_name: str) -> List[str]:
    with open(file_name) as file:
        return file.read().splitlines(keepends=True)


def write_lines(file_name: str, lines: List[str]):
    with open(file_name, "w") as file:
        file.writelines(lines)
