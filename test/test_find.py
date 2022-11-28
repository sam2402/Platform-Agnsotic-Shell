import os
import shutil
import unittest
from collections import deque

import src.applications.find as find
from src.applications.application import ArgumentError


class TestFind(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "FindFolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.files = ["file1.txt", "file2.txt", "file3.txt"]
        for file in self.files:
            with open(os.path.join(self.folder, file), 'w') as f:
                pass

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def test_find_no_args(self):
        self.assertRaises(ArgumentError, find.Find.run, self, [], self.out, [])

    def test_find_no_name_flag(self):
        self.assertRaises(ArgumentError, find.Find.run, self, [], self.out, ["-notname", "file"])

    def test_find_one_file(self):
        find.Find.run(self, [], self.out, ["-name", self.files[0]])
        self.assertEqual(self.out.popleft(), os.path.join(".", self.folder, self.files[0] + "\n"))

    def test_find_help_message(self):
        self.assertEqual(find.Find.help_message(self), "find [path] -name <pattern>")


if __name__ == '__main__':
    unittest.main()
