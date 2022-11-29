import filecmp
import os
import unittest

from applications.application import ApplicationError
from util import read_lines, write_lines


class TestUtil(unittest.TestCase):

    def setUp(self) -> None:
        self.out = []
        self.file_name = "file1.txt"
        self.text = "This is line number 1\n" \
                    "and this is the second line\n" \
                    "third line to check"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_file_doesnt_exist(self):
        with self.assertRaises(ApplicationError):
            read_lines("file2.txt")

    def test_read_lines(self):
        self.out = read_lines(self.file_name)
        expected_output = self.text.splitlines(keepends=True)
        for i in range(3):
            self.assertEqual(self.out, expected_output)

    def test_write_lines(self):
        file_to_write = "file2.txt"
        text_to_write = "This is line number 1\n" \
                        "and this is the second line\n" \
                        "third line to check".split("\n ")

        write_lines(file_to_write, text_to_write)
        self.assertEqual(filecmp.cmp(self.file_name, file_to_write,
                                     shallow=False), True)
        os.remove(file_to_write)
