import unittest
import src.applications.sort as sort
import os
from collections import deque

class TestSort(unittest.TestCase):

    def setUp(self) -> None:
        self.out = deque()
        self.file_name = "file1.txt"

        self.text = "This is a test file to see the sort working correctly. "
        self.text = self.text.replace(" ", "\n")

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_sort_normal(self):
        sort.Sort.run(self,[],self.out,["file1.txt"])
        text_to_check = "This a correctly. file is see sort test the to working".split()
        for i in range(len(text_to_check)):
            self.assertEqual(self.out.popleft(), text_to_check[i] + "\n")


    def test_sort_reverse(self):
        sort.Sort.run(self,[],self.out,["-r","file1.txt"])
        text_to_check = "working to the test sort see is file correctly. a This".split()
        for i in range(len(text_to_check)):
            self.assertEqual(self.out.popleft(), text_to_check[i] + "\n")

    def test_sort_help_message(self):
        self.assertEqual(sort.Sort.help_message(self), "sort [-r -R] [file]")


if __name__ == '__main__':
    unittest.main()
