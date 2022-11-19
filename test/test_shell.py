import unittest
from collections import deque

from shell import evaluate

from src.applications.echo import Echo
from src.applications.cat import Cat



class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        evaluate("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)


    def test_echo(self):
        self.assertEqual(Echo.help_message(),"echo [args...]")

    def test_cat(self):
        self.assertEqual(Cat.help_message(),"cat [files...]")







if __name__ == "__main__":
    unittest.main()
