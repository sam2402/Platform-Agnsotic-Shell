import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.application import ArgumentError
from src.applications.rm import Rm


class TestRm(ApplicationTest):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "RmFolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.files = ["file1.txt", "file2.txt", "file3.txt"]
        for file in self.files:
            with open(os.path.join(self.folder, file), 'w'):
                pass

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def test_zero_args(self):
        self.assertRaises(ArgumentError, Rm.run, self, [], self.out, [])

    def test_rm_normal(self):
        app_rm = Rm({"-r": False, "-v": False, "-f": False})
        file = os.path.join(self.folder, "file1.txt")
        app_rm.run([], self.out, [file])
        self.assertEqual(os.listdir(self.folder), ['file3.txt', 'file2.txt'])

    def test_rm_help_message(self):
        self.assertEqual(Rm.help_message(self),
                         "rm [-v -r -f] [directories/files...]")


if __name__ == '__main__':
    unittest.main()
