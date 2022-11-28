import unittest
from collections import deque

from src.shell import evaluate


class TestParser(unittest.TestCase):

    def test_parser(self):
        self.out = deque()
        evaluate("echo foo bar",self.out)
        self.assertEqual(self.out.popleft(),"foo bar\n")

if __name__ == '__main__':
    unittest.main()
