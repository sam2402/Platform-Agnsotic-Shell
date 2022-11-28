import os
import shutil
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.ls import Ls


class TestLs(ApplicationTest):

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "FolderHolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.folders = {"folder1", "folder2", "folder3", ".folder4", ".folder5"}
        for folder in self.folders:
            os.mkdir(os.path.join(self.folder,folder))


    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    def test_ls_zero_arg(self):
        self.out = deque()
        os.chdir(self.folder)
        app_ls = Ls({"-a": False, "-r": False, "-s": False})
        app_ls.run([], self.out, [])
        os.chdir("..")
        self.assertEqual(self.out.popleft(), "folder1\tfolder2\tfolder3\n")

    def test_ls_show_hidden(self):
        self.out = deque()
        os.chdir(self.folder)
        app_ls = Ls({"-a": True, "-r": False, "-s": False})
        app_ls.run([], self.out, [])
        os.chdir("..")
        result = self.out.popleft()
        for item in self.folders:
            self.assertIn(item, result)

    def test_ls_not_dir(self):
        self.out = deque()
        app_ls = Ls({"-a": False, "-r": False, "-s": False})
        app_ls.run([], self.out, [self.folder])
        self.assertEqual(self.out.popleft(), "folder1\tfolder2\tfolder3\n")

    def test_ls_help_message(self):
        self.assertEqual(Ls.help_message(self), "ls [-a -r -s] [directory]")


if __name__ == '__main__':
    unittest.main()
