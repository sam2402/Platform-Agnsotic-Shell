import unittest
import src.applications.uniq as uniq
import os
import shutil
from collections import deque

class TestUniq(unittest.TestCase):
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
            with open(os.path.join(self.folder, file),"x") as f:
                f.write(self.files[file])

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def test_uniq_help_message(self):
        self.assertEqual(uniq.Uniq.help_message(self), "uniq [-i] [file]")


if __name__ == '__main__':
    unittest.main()
