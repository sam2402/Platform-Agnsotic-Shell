import os
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.application import ArgumentError, ApplicationError
from src.applications.grep import Grep


class TestGrep(ApplicationTest):
    def setUp(self) -> None:
        self.app_grep = Grep({"-v": False})
        self.out = deque()
        self.file_name = "file1.txt"
        self.text = "This is the first line\nand this is the second line\ngrep method\n"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_grep_no_args(self):
        self.assertRaises(ArgumentError, Grep.run, self, [], self.out, [])

    def test_grep_invalid_args(self):
        self.assertRaises(ApplicationError, Grep.run, self, [], self.out, ["66s\\55a",self.file_name])

    def test_grep_one_valid_arg(self):
        self.app_grep.run([], self.out, ["second", self.file_name])
        self.assertEqual(self.out.popleft(),"and this is the second line\n")

    def test_grep_multiple_valid_arg(self):
        self.app_grep.run([], self.out, ["line", self.file_name])
        ans = ["This is the first line\n","and this is the second line\n"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i])

    '''
    def test_grep_stdin(self):
        grep.Grep.run(self,[self.file_name],self.out,["second"])
        self.assertEqual(self.out.popleft(),"and this is the second line\n")
    '''

    def test_grep_help_message(self):
        self.assertEqual(Grep.help_message(self), "grep [-v] <pcre> [files...]")


if __name__ == '__main__':
    unittest.main()
