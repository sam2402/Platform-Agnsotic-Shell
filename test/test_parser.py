import unittest
from collections import deque
from src.parser import execute_command
import os


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.out_list = []
        self.file_name = "file1.txt"
        self.text = "Uniq method test\nUniq method test\nUniQ MethoD TesT\n"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_double_quote(self):
        self.out_list = execute_command("echo \"foo bar\"")
        self.assertEqual(self.out_list, ["foo bar\n"])

    def test_single_quote(self):
        self.out_list = execute_command("echo \'foo bar\'")
        self.assertEqual(self.out_list, ["foo bar\n"])

    #def test_back_quote(self):

    def test_pipe_commands(self):
        self.out_list = execute_command("cat file1.txt | uniq -i")
        self.assertEqual(self.out_list, ["Uniq method test\n"])


if __name__ == '__main__':
    unittest.main()
