from abc import ABC, abstractmethod
from typing import Deque, List, Type

from flagging import ApplicationFlagDict, FlagConfiguration


class Application(ABC):
    """Base class for all runnable applications

    Provides common util functions that are class dependant

    Attributes:
        name - static: name of application used in terminal as string
        flag_configuration - static: FlagConfiguration object specifying which
            flags an application accepts
            By default, all applications accept the -h (help) flag
        flags: a dictionary of all flag values
            Configured by flag_configuration
    """

    name: str
    flag_configuration: FlagConfiguration = FlagConfiguration()

    @classmethod
    def clean_args(cls, args: List[str]) -> List[str]:
        """Removes the application name, flags and their parameters

        Args:
            args: A list of args as strings
                It is assumed the first element in the list is the application
                name

        Returns:
            A list of arguments with the application name, flags and their
            parameters removed
        """
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
        """Runs the application with flag context

        Args:
            inp: standard input - a list of strings from which a program reads
                its input data
            out: standard output - a dequeue of strings to which a program
                writes its output data
            args: command line arguments - a list of strings that can alter
                the operation of a program
                see the help_message function to see which args are accepted
                for each application

        Raises:
            ArgumentError: the flags and/or args are malformed
            ApplicationError: an error occurred in the execution of the command
        """

    @abstractmethod
    def help_message(self) -> str:
        """Details the syntax of the application's command

        square brackets (`[]`) around a parameter means the parameter is
        optional
        an ellipsis `...` after a parameter is equivalent to the Kleene star

        example: `echo [-n] [args...]` is an `echo` command that can take a
            `-n` flag and 0 or more args.
            `echo -n arg1 arg2 arg3` is valid

        Returns:
            A string detailing the syntax of the application's command
        """


class UnsafeApplication(Application):
    """An adapter pattern implementation Application class to provide an unsafe
    variant

    An unsafe version of an application is an application that has the same
    semantics as the original application, but instead of raising exceptions,
    it prints the error message to its stdout
    """

    def __init__(self, child_application: Application):
        super().__init__(child_application.flags)
        self._child_application = child_application

    def run(self, inp: List[str], out: Deque[str], args: List[str]):
        try:
            self._child_application.run(inp, out, args)
        except Exception as err:
            out.append(str(err) + "\n")

    def help_message(self) -> str:
        return self._child_application.help_message()


class ArgumentError(Exception):
    """Raised when an application is called with the incorrect arguments"""

    def __init__(self, application_type: Type[Application], *args):
        super().__init__(*args)
        self._application_type = application_type

    def __str__(self) -> str:
        return f"{self._application_type.name} - {super().__str__()}"


class ApplicationError(Exception):
    """Raised when an error occurs when calling an application"""
