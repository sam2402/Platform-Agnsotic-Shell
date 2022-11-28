import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest, application_test
from src.applications.application import ArgumentError
from src.applications.find import Find


class TestFind(ApplicationTest):
    application = Find

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "FindFolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.files = ["file1.txt", "file2.txt", "file3.txt"]
        for file in self.files:
            with open(os.path.join(self.folder, file), 'w'):
                pass

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    @application_test()
    def test_find_no_args(self):
        self.assertRaises(ArgumentError, Find.run, self, [], self.out, [])

    @application_test()
    def test_find_no_name_flag(self):
        self.assertRaises(ArgumentError, Find.run, self, [], self.out,
                          ["-notname", "file"])

    @application_test()
    def test_find_one_file(self):
        Find.run(self, [], self.out, ["-name", self.files[0]])
        file_address = os.path.join(".", self.folder, self.files[0] + "\n")
        self.assertEqual(self.out.popleft(), file_address)

    @application_test()
    def test_find_help_message(self):
        self.assertEqual(Find.help_message(self), "find [path] -name "
                                                       "<pattern>")


if __name__ == '__main__':
    unittest.main()
