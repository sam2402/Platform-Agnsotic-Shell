from abc import ABC, abstractmethod
from typing import Deque, List


class Application(ABC):

    @abstractmethod
    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        pass

    @abstractmethod
    def help_message(self) -> str:
        pass


class UnsafeApplication(Application):

    def __init__(self, child_application: Application):
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
