import unittest
import src.applications.uniq as uniq
import os
import shutil
from collections import deque

class TestUniq(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.file_name = "file1.txt"
        self.text = "Uniq method test\nUniq method test\nUniQ MethoD TesT\n"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_uniq_no_options(self):
        uniq.Uniq.run(self,[],self.out,[self.file_name])
        ans = ["Uniq method test\n","UniQ MethoD TesT\n"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i])

    def test_uniq_case_insensitive(self):
        uniq.Uniq.run(self,[],self.out,["-i",self.file_name])
        self.assertEqual(self.out.popleft(), "Uniq method test\n")

    def test_uniq_help_message(self):
        self.assertEqual(uniq.Uniq.help_message(self), "uniq [-i] [file]")


if __name__ == '__main__':
    unittest.main()
