from abc import ABC, abstractmethod
from typing import Deque, List

from flagging import ApplicationFlagDict, FlagConfiguration


class Application(ABC):

    flag_configuration: FlagConfiguration = FlagConfiguration()

    @classmethod
    def clean_args(cls, args: List[str]):
        i = 1
        while i < len(args):
            arg = args[i]
            if arg in cls.flag_configuration:
                i += cls.flag_configuration[arg].argument_count
            else:
                return args[i:]
            i += 1
        return []

    def __init__(self, flags: ApplicationFlagDict = None):
        self.flags = flags or {}

    @abstractmethod
    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        pass

    @abstractmethod
    def help_message(self) -> str:
        pass


class UnsafeApplication(Application):

    def __init__(self, child_application: Application):
        super().__init__(child_application.flags)
        self.child_application = child_application

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        try:
            self.child_application.run(inp, out, args)
        except Exception as err:
            out.append(str(err) + "\n")

    def help_message(self) -> str:
        return self.child_application.help_message()


# Raised when an application is called with the incorrect arguments
class ArgumentError(Exception):
    pass


# Raised when an error occurs when calling an application
class ApplicationError(Exception):
    pass
