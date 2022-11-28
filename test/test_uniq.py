import os
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.uniq import Uniq


class TestUniq(ApplicationTest):
    def setUp(self) -> None:
        self.out = deque()
        self.app_uniq = Uniq({"-i": False})
        self.file_name = "file1.txt"
        self.text = "Uniq method test\nUniq method test\nUniQ MethoD TesT\n"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    def test_uniq_no_options(self):
        self.app_uniq.run([], self.out, [self.file_name])
        ans = ["Uniq method test\n", "UniQ MethoD TesT\n"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i])

    def test_uniq_case_insensitive(self):
        app_uniq_i = Uniq({"-i": True})
        app_uniq_i.run([], self.out, [self.file_name])
        self.assertEqual(self.out.popleft(), "Uniq method test\n")

    def test_uniq_help_message(self):
        self.assertEqual(Uniq.help_message(self), "uniq [-i] [file]")


if __name__ == '__main__':
    unittest.main()
