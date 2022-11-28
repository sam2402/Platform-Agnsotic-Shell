import os
import unittest
from collections import deque

from application_test import ApplicationTest, application_test
from src.applications.sort import Sort


class TestSort(ApplicationTest):

    application = Sort

    def setUp(self) -> None:
        self.out = deque()
        self.file_name = "file1.txt"

        self.text = "This is a test file to see the sort working correctly. "
        self.text = self.text.replace(" ", "\n")

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    @application_test({"-r": False, "-R": False})
    def test_sort_normal(self, sort):
        sort.run([], self.out, ["file1.txt"])
        text_to_check = "This a correctly. file is see sort test the to " \
                        "working".split()
        for i in range(len(text_to_check)):
            self.assertEqual(self.out.popleft(), text_to_check[i] + "\n")

    @application_test({"-r": True, "-R": False})
    def test_sort_reverse(self, sort):
        sort.run([], self.out, ["file1.txt"])
        text_to_check = "working to the test sort see is file correctly. a " \
                        "This".split()
        for i in range(len(text_to_check)):
            self.assertEqual(self.out.popleft(), text_to_check[i] + "\n")

    @application_test({"-r": False, "-R": True})
    def test_sort_random(self, sort):
        sort.run([], self.out, ["file1.txt"])
        text_to_check = "This a correctly. file is see sort test the to " \
                        "working".split()
        text_to_check = [s + "\n" for s in text_to_check]
        for i in range(len(text_to_check)):
            self.assertIn(self.out.popleft(), text_to_check)

    def test_sort_help_message(self):
        self.assertEqual(Sort.help_message(self), "sort [-r -R] [file]")


if __name__ == '__main__':
    unittest.main()
