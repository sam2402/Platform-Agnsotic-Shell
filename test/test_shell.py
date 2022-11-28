import unittest
from collections import deque
from src.shell import evaluate


class TestShell(unittest.TestCase):
    def test_shell_empty(self):
        out = deque()
        evaluate("",out)
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    unittest.main()
