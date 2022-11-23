import unittest
import src.applications.find as find
import os
import shutil
from collections import deque

class TestFind(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
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
        shutil.rmtree(self.folder)

    def test_find_help_message(self):
        self.assertEqual(find.Find.help_message(self), "find [path] -name <pattern>")


if __name__ == '__main__':
    unittest.main()
