import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from applications.application import ArgumentError
from applications.find import Find


class TestFind(ApplicationTest):
    application = Find

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "FindFolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.files = ["file1.txt", "file2.txt", "file3.txt"]
        for file in self.files:
            with open(os.path.join(self.folder, file), 'w'):
                pass

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    @application_test()
    def test_find_no_args(self, find):
        with self.assertRaises(ArgumentError):
            find.run([], self.out, [])

    @application_test()
    def test_find_no_name_flag(self, find):
        with self.assertRaises(ArgumentError):
            find.run([], self.out, ["-notname", "file"])

    @application_test()
    def test_find_one_file(self, find):
        find.run([], self.out, ["-name", self.files[0]])
        file_address = os.path.join(".", self.folder, self.files[0] + "\n")
        self.assertEqual(self.out.popleft(), file_address)

    @application_test({"-h": True})
    def test_find_help_message(self, find):
        self.assertEqual(find.help_message(), "find [path] -name "
                         "<pattern>")
