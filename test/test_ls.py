import unittest
import src.applications.ls as ls
import os
import shutil
from collections import deque
import re
from system_test.tests import TestShell

from src.shell import evaluate

import re
from system_test.tests import TestShell


class TestLs(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()


        self.folder = "TestFolder"
        self.dir_name = os.getcwd() + "/" + self.folder

        self.folder = "TestFiles"

        self.folder = "TestFiles"

        if not os.path.exists(self.folder):
            os.mkdir(self.folder)

        self.files = {
            "file1.txt": "this\nis\nfile\nnumber\none",
            "file2.txt": "and\nthis\nis\nthe\nsecond\nfile",
            "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles"
        }

        for file in self.files:
            with open(os.path.join(self.folder, file), "x") as f:
                f.write(self.files[file])

    def tearDown(self) -> None:

        shutil.rmtree(self.dir_name)

        shutil.rmtree(self.folder)


    def test_ls_zero_arg(self):
        self.out = deque()
        os.chdir(self.folder)

        evaluate("ls")
        self.assertEqual(self.out.popleft(), "folder1\tfolder2\tfolder3\n")
        #os.chdir("..")

        ls.Ls.run(self, [], self.out, [])
        self.assertEqual(self.out.popleft(), os.listdir() + "\n")
        ls.Ls.run(self, [], self.out, [])
        self.assertEqual(self.out.popleft(), os.listdir() + "\n")



    def test_ls_help_message(self):
        self.assertEqual(ls.Ls.help_message(self), "ls [-a] [directory]")


if __name__ == '__main__':
    unittest.main()
