import unittest
import src.applications.cd as cd
import os
from collections import deque
from src.applications.application import ArgumentError
import shutil


class TestCd(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFolder"
        self.dir_name = os.getcwd() + "\\" + self.folder
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
            os.chdir(self.folder)

            self.folders = {"folder1", "folder2", "folder3"}

            for folder in self.folders:
                os.mkdir(folder)
            os.chdir("..")


    def tearDown(self) -> None:
        shutil.rmtree(self.dir_name)

    def test_cd_zero_arg(self):
        self.out = deque()
        self.assertRaises(ArgumentError, cd.Cd.run, self, [], self.out, [])

    def test_cd_one_valid_arg(self):
        self.out = deque()
        cd.Cd.run(self, [], self.out, [self.folder])
        self.assertEqual(os.getcwd(),self.dir_name)

    def test_cd_help_message(self):
        self.assertEqual(cd.Cd.help_message(self), "cd <directory>")


if __name__ == '__main__':
    unittest.main()
