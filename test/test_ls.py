import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest, application_test
from src.applications.application import ApplicationError
from src.applications.ls import Ls


class TestLs(ApplicationTest):

    application = Ls

    def setUp(self):
        self.out = deque()
        self.folder = "FolderHolder"
        self.file = "file1.txt"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.folders = {"folder1", "folder2", "folder3", ".folder4",
                        ".folder5"}
        for folder in self.folders:
            os.mkdir(os.path.join(self.folder, folder))

        os.chdir(self.folder)
        _ = open(self.file, 'w')

    def tearDown(self):
        os.chdir("..")
        shutil.rmtree(self.folder)

    @application_test({"-a": False, "-r": False, "-s": False})
    def test_ls_zero_arg(self, ls):
        ls.run([], self.out, [])
        result = self.out.popleft()
        paths = {
            *filter(lambda file: not file.startswith("."), self.folders),
            self.file
        }
        for path in paths:
            self.assertIn(path, result)

    @application_test({"-a": True, "-r": False, "-s": False})
    def test_ls_show_hidden(self, ls):
        ls.run([], self.out, [])
        result = self.out.popleft()
        for folder in self.folders:
            self.assertIn(folder, result)

    @application_test({"-a": True, "-r": False, "-s": True})
    def test_ls_s_flag(self, ls):
        ls.run([], self.out, [])
        result = self.out.popleft()
        for folder in self.folders:
            self.assertIn(f"0 {folder}", result)

    @application_test({"-a": False, "-r": True, "-s": False})
    def test_ls_r_flag(self, ls):
        ls.run([], self.out, [])
        result = self.out.popleft()
        paths = {
            *filter(lambda file: not file.startswith("."), self.folders),
            self.file
        }
        for path in paths:
            self.assertIn(path, result)

    @application_test({"-a": False, "-r": False, "-s": False})
    def test_ls_file(self, ls):
        with self.assertRaises(ApplicationError):
            ls.run([], self.out, ["fake_file.txt"])

    @application_test({"-a": False, "-r": False, "-s": False})
    def test_ls_file_in_empty_directry(self, ls):
        ls.run([], self.out, ["folder1"])
        self.assertEqual(self.out, deque())

    @application_test({"-h": True})
    def test_ls_help_message(self, ls):
        self.assertEqual(ls.help_message(), "ls [-a -r -s] [directory]")


if __name__ == '__main__':
    unittest.main()
