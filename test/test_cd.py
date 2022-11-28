import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.application import ArgumentError
from src.applications.cd import Cd


class TestCd(ApplicationTest):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)


    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def test_cd_zero_arg(self):
        self.assertRaises(ArgumentError, Cd.run, self, [], self.out, [])

    def test_cd_one_valid_arg(self):
        self.out = deque()
        Cd.run(self,[],self.out,[self.folder])
        self.assertEqual(os.getcwd(),self.dir_name)
        os.chdir("..")

    def test_cd_help_message(self):
        self.assertEqual(Cd.help_message(self), "cd <directory>")


if __name__ == '__main__':
    unittest.main()
