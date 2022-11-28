import unittest
from collections import deque

from src.shell import evaluate


class TestShell(unittest.TestCase):

    def test_shell_standard(self):
        out = deque()
        evaluate("echo foo bar", out)
        self.assertEqual(out.popleft(), "foo bar\n")

    def test_shell_unsafe_application(self):
        out = deque()
        evaluate("_echo foo bar", out)
        self.assertEqual(out.popleft(), "foo bar\n")


if __name__ == "__main__":
    unittest.main()
