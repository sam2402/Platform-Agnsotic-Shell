import unittest
from collections import deque

from parameterized import parameterized

from application_test import ApplicationTest, application_test
from src.applications.echo import Echo


class TestEcho(ApplicationTest):
    application = Echo

    @parameterized.expand([
        [[], deque(), deque(["foo", "bar"]), deque(["foo bar\n"])],
        [[], deque(), deque(["foo", "bar", "baz"]), deque(["foo bar baz\n"])],
        [[], deque(), deque([]), deque(["\n"])],
        [[], deque(), deque(["some sentence"]), deque(["some sentence\n"])],
    ])
    @application_test(flags={"-n": False})
    def test_echo_run_with_newlines(self, echo, inp, out, args, expected_out):
        echo.run(inp, out, args)
        self.assertEqual(out, expected_out)

    @parameterized.expand([
        [[], deque(), deque(["foo", "bar"]), deque(["foo bar"])],
        [[], deque(), deque(["foo", "bar", "baz"]), deque(["foo bar baz"])],
        [[], deque(), deque([]), deque([""])],
        [[], deque(), deque(["some sentence"]), deque(["some sentence"])],
    ])
    @application_test(flags={"-n": True})
    def test_echo_run_without_newlines(self, echo, inp, out,
                                       args, expected_out):
        echo.run(inp, out, args)
        self.assertEqual(out, expected_out)

    @application_test({"-h": True})
    def test_echo_help_message(self, echo):
        self.assertEqual(echo.help_message(), "echo [-n] [args...]")


if __name__ == "__main__":
    unittest.main()
