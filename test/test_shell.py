import unittest
from collections import deque

from shell import evaluate


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        evaluate("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    unittest.main()
