"""Module of classes used to represent the types of command"""

import os
from abc import ABC, abstractmethod
from collections import deque

import util
from application_factory import ApplicationFactory
from applications.application import ApplicationError


class SubCommand(ABC):

    @abstractmethod
    def execute(self, inp: list[str]) -> list[str]:
        """Run execute the command

        Args:
            inp: list of strings representing stdin
        """


class CallCommand(SubCommand):

    def __init__(self, args: list[str], in_file: str, out_file: str):
        self.args = args
        self.in_file = in_file
        self.out_file = out_file

    def execute(self, inp: list[str]) -> list[str]:
        if self.in_file and not inp:
            if not os.path.exists(self.in_file):
                raise ApplicationError(
                    f"input file '{self.in_file}' does not exist"
                )
            inp = util.read_lines(self.in_file)

        application = ApplicationFactory().get_application(self.args)
        out = deque()
        if application.flags["-h"]:
            out.append(f"{application.help_message()}\n")
        else:
            cleaned_args = application.clean_args(self.args)
            application.run(inp, out, cleaned_args)

        if self.out_file:
            util.write_lines(self.out_file, list(out))
            return []

        return list(out)


class PipeCommand(SubCommand):

    def __init__(self, call: CallCommand, receiver: SubCommand):
        self.call = call
        self.receiver = receiver

    def execute(self, inp: list[str]) -> list[str]:
        out = self.call.execute(inp)
        return self.receiver.execute(out)


class Command:

    def __init__(self, sub_commands: list[SubCommand]):
        self.sub_commands = sub_commands

    def execute(self) -> list[str]:
        out = [line
               for sub_command in self.sub_commands
               for line in sub_command.execute([])]
        return out
