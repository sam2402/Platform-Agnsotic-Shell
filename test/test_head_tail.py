import unittest
import src.applications.head_tail as head_tail
import os
import shutil
from collections import deque

class TestHeadTail(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFiles"
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

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

    def test_head_tail_help_message(self):
        self.assertEqual(head_tail.Head.help_message(self), "head [-n lines] [file]")
        self.assertEqual(head_tail.Tail.help_message(self), "tail [-n lines] [file]")


if __name__ == '__main__':
    unittest.main()
