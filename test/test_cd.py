import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest, application_test
from src.applications.application import ArgumentError, ApplicationError
from src.applications.cd import Cd


class TestCd(ApplicationTest):
    application = Cd

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFolder"
        self.file = "TestFile"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        with open(self.file, 'w'):
            pass

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)
        os.remove(self.file)

    @application_test()
    def test_cd_zero_arg(self):
        self.assertRaises(ArgumentError, Cd.run, self, [], self.out, [])

    @application_test()
    def test_cd_one_valid_arg(self):
        Cd.run(self, [], self.out, [self.folder])
        self.assertEqual(os.getcwd(), self.dir_name)
        os.chdir("..")

    @application_test()
    def test_cd_file(self):
        self.assertRaises(ApplicationError, Cd.run, self, [], self.out,
                          [self.file])

    @application_test()
    def test_cd_help_message(self):
        self.assertEqual(Cd.help_message(self), "cd <directory>")


if __name__ == '__main__':
    unittest.main()
