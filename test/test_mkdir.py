import unittest
import src.applications.mkdir as mkdir
import os
from collections import deque
from src.shell import evaluate
from src.applications.application import ApplicationError


class TestMkdir(unittest.TestCase):

    def test_mkdir_one_directory(self):
        self.out = deque
        evaluate("mkdir folder7", self.out)
        self.assertIn("folder7", os.listdir())

    def test_mkdir_multiple_directories(self):
        self.out = deque
        self.assertRaises(ApplicationError, evaluate("mkdir dr1", self.out))

    def test_mkdir_multiple_directories(self):
        self.out = deque
        evaluate("mkdir folder4 folder5 folder6", self.out)
        dirs = {"folder4", "folder5", "folder6"}
        listdir = os.listdir()
        for directory in dirs:
            self.assertIn(directory, listdir)

    def test_mkdir_help_message(self):
        self.assertEqual(mkdir.Mkdir.help_message(self), "mkdir [directories...]")


if __name__ == '__main__':
    unittest.main()
