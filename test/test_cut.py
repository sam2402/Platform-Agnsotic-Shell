import os
import unittest
from collections import deque
from application_test import ApplicationTest
from src.applications.application import ArgumentError
from src.applications.cut import Cut


class TestCut(ApplicationTest):
    def setUp(self) -> None:
        self.out = deque()
        self.file_name = "file1.txt"
        self.text = "This is the first line\nand this is the second line\ncut method test\n"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_cut_no_flag(self):
        self.assertRaises(ArgumentError, Cut.run, self, [], self.out, ["1,","2"])

    def test_cut_valid(self):
        app_cut = Cut({"-b": "1"})
        app_cut.run([], self.out, [self.file_name])
        ans = ["T","a","c"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i] + "\n")

    def test_cut_valid_range(self):
        app_cut = Cut({"-b": "1-3"})
        app_cut.run([], self.out, [self.file_name])
        ans = ["Thi","and","cut"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i] + "\n")

    def test_cut_starting_and_ending_with_flag(self):
        app_cut = Cut({"-b": "-2,5-"})
        app_cut.run([], self.out, [self.file_name])
        ans = ["Th is the first line","anthis is the second line","cumethod test"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i] + "\n")

    def test_cut_help_message(self):
        self.assertEqual(Cut.help_message(self), "cut -b <intervals> [file]")


if __name__ == '__main__':
    unittest.main()
