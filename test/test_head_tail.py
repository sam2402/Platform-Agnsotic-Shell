import unittest
import src.applications.head_tail as head_tail
import os
from collections import deque


class TestHeadTail(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.file_name = "file1.txt"
        self.text = "This is a test file to see the head and tail function working correctly. Since the functions "\
                    "work on the contents of a file, we generate a file to contain text can can be checked " \
                    "against. "
        self.text = self.text.replace(" ", "\n")

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_head_no_input(self):
        head_tail.Head.run(self,[],self.out,["file1.txt"])
        self.text_to_check = "This is a test file to see the head and".split()

        for i in range(10):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_head_5_lines(self):
        head_tail.Head.run(self,[],self.out,["-n","5","file1.txt"])
        self.text_to_check = "This is a test file".split()

        for i in range(5):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_tail_no_input(self):
        head_tail.Tail.run(self, [], self.out,["file1.txt"])
        self.text_to_check = "a file to contain text can can be checked against.".split()

        for i in range(10):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_tail_5_lines(self):
        head_tail.Tail.run(self, [], self.out, ["-n", "5", "file1.txt"])
        self.text_to_check = "can can be checked against.".split()

        for i in range(5):
            self.assertEqual(self.out.popleft(), self.text_to_check[i] + "\n")

    def test_head_help_message(self):
        self.assertEqual(head_tail.Head.help_message(self), "head [-v -n lines] [file]")

    def test_tail_help_message(self):
        self.assertEqual(head_tail.Tail.help_message(self), "tail [-v -n lines] [file]")


if __name__ == '__main__':
    unittest.main()
