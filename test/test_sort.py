import unittest
import src.applications.sort as sort
import os
import shutil
from collections import deque

class TestSort(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFiles"
        self.dir_name = os.getcwd() + "/" + self.folder
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
            os.chdir(self.folder)

            self.files = {
                "file1.txt": "this\nis\nfile\nnumber\none",
                "file2.txt": "and\nthis\nis\nthe\nsecond\nfile",
                "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles"
            }

            for file in self.files:
                with open(os.path.join(self.dir_name, file), "x") as f:
                    f.write(self.files[file])

    def tearDown(self) -> None:
        shutil.rmtree(self.dir_name)

    def test_sort_help_message(self):
        self.assertEqual(sort.Sort.help_message(self), "sort [-r] [file]")


if __name__ == '__main__':
    unittest.main()
