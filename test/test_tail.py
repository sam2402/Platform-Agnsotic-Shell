import os
import unittest
from collections import deque

from application_test import ApplicationTest, application_test
from src.applications.head_tail import Tail


class TestTail(ApplicationTest):
    application = Tail

    def setUp(self) -> None:
        self.out = deque()
        self.file_name = "file1.txt"
        self.text = "This is a test file to see the head and tail function " \
                    "working correctly. Since the functions work on the " \
                    "contents of a file, we generate a file to contain text " \
                    "can can be checked against. "

        self.text = self.text.replace(" ", "\n")

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    @application_test(flags={"-n": 10, "-v": False})
    def test_tail_no_input(self, tail):
        tail.run([], self.out, ["file1.txt"])
        self.text_to_check = "a file to contain text can can be checked " \
                             "against.".split()

        for i in range(10):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    @application_test(flags={"-n": 5, "-v": False})
    def test_tail_5_lines(self, tail):
        tail.run([], self.out, ["file1.txt"])
        self.text_to_check = "can can be checked against.".split()

        for i in range(5):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    @application_test(flags={"-n": 10, "-v": True})
    def test_tail_v_flag(self, tail):
        tail.run([], self.out, ["file1.txt"])
        self.text_to_check = "==>file1.txt<==\n a file to contain text can " \
                             "can be checked against.".split()

        for i in range(10):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    @application_test()
    def test_tail_help_message(self, tail):
        self.assertEqual(tail.help_message(), "tail [-v -n lines] [file]")


if __name__ == '__main__':
    unittest.main()
