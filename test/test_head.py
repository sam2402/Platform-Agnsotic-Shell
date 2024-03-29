import os
from collections import deque

from application_test import ApplicationTest
from applications.application import ArgumentError
from applications.head_tail import Head


class TestHead(ApplicationTest):

    application = Head

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

    def test_head_no_input(self):
        app_head = Head({"-n": 10, "-v": False})
        app_head.run([], self.out, ["file1.txt"])
        self.text_to_check = "This is a test file to see the head and".split()

        for i in range(10):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_head_5_lines(self):
        app_head = Head({"-n": 5, "-v": False})
        app_head.run([], self.out, ["file1.txt"])
        self.text_to_check = "This is a test file".split()

        for i in range(5):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_head_v_flag(self):
        app_head = Head({"-n": 10, "-v": True})
        app_head.run([], self.out, ["file1.txt"])
        self.text_to_check = "==>file1.txt<==\n This is a test file to see " \
                             "the head and".split()

        for i in range(10):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_more_than_one_file(self):
        app_head = Head({"-n": 10, "-v": False})
        self.assertRaises(ArgumentError, app_head.run, [], self.out,
                          ["file1.txt", "file2.txt"])

    def test_head_help_message(self):
        self.assertEqual(Head.help_message(self), "head [-v -n lines] [file]")
