import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from applications.application import ArgumentError, ApplicationError
from applications.cd import Cd


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
    def test_cd_zero_arg(self, cd):
        with self.assertRaises(ArgumentError):
            cd.run([], self.out, [])

    @application_test()
    def test_cd_one_valid_arg(self, cd):
        cd.run([], self.out, [self.folder])
        self.assertEqual(os.getcwd(), self.dir_name)
        os.chdir("..")

    @application_test()
    def test_cd_file(self, cd):
        with self.assertRaises(ApplicationError):
            cd.run([], self.out, [self.file])

    @application_test()
    def test_cd_help_message(self, cd):
        self.assertEqual(cd.help_message(), "cd <directory>")
