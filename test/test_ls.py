import unittest
import src.applications.ls as ls
import os
import shutil
from collections import deque
from src.shell import evaluate

class TestLs(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFolder"
        self.dir_name = os.getcwd() + "/" + self.folder
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
            os.chdir(self.folder)

            self.folders = {"folder1", "folder2", "folder3"}

            for folder in self.folders:
                os.mkdir(folder)
            os.chdir("..")

    def tearDown(self) -> None:
        shutil.rmtree(self.dir_name)


    def test_ls_zero_arg(self):
        self.out = deque()
        os.chdir(self.folder)
        evaluate("ls")
        self.assertEqual(self.out.popleft(), "folder1\tfolder2\tfolder3\n")
        #os.chdir("..")


    def test_ls_help_message(self):
        self.assertEqual(ls.Ls.help_message(self), "ls [-a] [directory]")


if __name__ == '__main__':
    unittest.main()
