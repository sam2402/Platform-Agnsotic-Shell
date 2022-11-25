import unittest
import src.applications.mkdir as mkdir
import os
import shutil
from collections import deque
from src.applications.application import ApplicationError


class TestMkdir(unittest.TestCase):

    def setUp(self) -> None:
        self.out = deque()
        self.already_exists  = "dir1"
        os.mkdir(self.already_exists)

    def tearDown(self) -> None:
        shutil.rmtree(self.already_exists)

    def test_mkdir_one_directory(self):
        mkdir.Mkdir.run(self,[],self.out,["folder7"])
        self.assertIn("folder7", os.listdir())
        shutil.rmtree("folder7")

    def test_mkdir_dir_already_exists(self):
        self.assertRaises(ApplicationError, mkdir.Mkdir.run, self, [], self.out, [self.already_exists])

    def test_mkdir_multiple_directories(self):
        mkdir.Mkdir.run(self, [], self.out, ["folder4", "folder5", "folder6"])
        dirs = {"folder4", "folder5", "folder6"}
        listdir = os.listdir()
        for directory in dirs:
            self.assertIn(directory, listdir)
        for dir in dirs:
            shutil.rmtree(dir)

    def test_mkdir_help_message(self):
        self.assertEqual(mkdir.Mkdir.help_message(self), "mkdir [directories...]")


if __name__ == '__main__':
    unittest.main()
