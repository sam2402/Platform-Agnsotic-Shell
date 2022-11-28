import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.cat import Cat


class TestCat(ApplicationTest):

    def setUp(self) -> None:
        self.app_cat = Cat({"-n": False})
        self.out = deque()
        self.folder = "TestFiles"
        os.mkdir(self.folder)

        self.files = {
            "file1.txt": "this\nis\nfile\nnumber\none\n",
            "file2.txt": "and\nthis\nis\nthe\nsecond\nfile\n",
            "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles\n"
        }

        for filename, content in self.files.items():
            with open(os.path.join(self.folder, filename), "x") as f:
                f.write(content)

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def test_cat_valid_file(self):
        arg = os.path.join(self.folder,"file1.txt")
        self.app_cat.run([],self.out,[arg])
        ans = self.files["file1.txt"].split()
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i] + "\n")


    def test_cat_stdin(self):
        text = "This is a default message to test cat function".split()
        self.app_cat.run(text, self.out, [])
        for i in range(len(text)):
            self.assertEqual(self.out.popleft(), text[i])

    def test_cat_help_message(self):
        self.assertEqual(Cat.help_message(self), "cat [-n] [files...]")


if __name__ == '__main__':
    unittest.main()
