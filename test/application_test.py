import functools
import unittest
from abc import ABC
from typing import Callable, Type

from flagging import ApplicationFlagDict
from src.applications.application import Application


class ApplicationTest(unittest.TestCase, ABC):
    """Base class for all application unit tests

    Attributes:
        application - static: The concrete class of the application being
            tested
    """

    application: Type[Application]

    def get_application(self, flags: ApplicationFlagDict) -> Application:
        """Get an object of the application

        Defaults to setting the help flag to false
        """
        return self.application({"-h": False} | flags)


def application_test(flags: ApplicationFlagDict = {}) -> Callable:
    """Decorator for the test application methods

    Adds an object of the application class instantiated with the provided
    flags as the first argument after self

    Example:

    class TestEcho(ApplicationTest):

    application = Echo

    @application_test(flags={"-n": False, "-s": "some value"})
    def test_echo_run(self, echo: Echo):
        echo.flags # {"-n": False, "-s": "some value"}
        out = deque()
        echo.run([], out, ["foo", "bar"])
        self.assertEqual(out.popleft(), "foo bar" + "\n")
    """

    def application_flag_decorator(function):
        @functools.wraps(function)
        def wrap_function(self: ApplicationTest, *args, **kwargs):
            app_with_flags = self.get_application(flags)
            return function(self, app_with_flags, *args, **kwargs)

        return wrap_function

    return application_flag_decorator
