import unittest
from collections import deque
from src.shell import evaluate
from src.parser import ParsingError
from src.applications.application import ApplicationError


class TestShell(unittest.TestCase):
    # def test_shell_empty(self):
    #    out = deque()
    #    self.assertRaises(ParsingError, evaluate, "", out)

    def test_shell_invalid_command(self):
        out = deque()
        self.assertRaises(ApplicationError, evaluate, "???", out)


if __name__ == "__main__":
    unittest.main()
