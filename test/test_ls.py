import os
import shutil
import unittest
from collections import deque
from src.applications.application import ApplicationError
from application_test import ApplicationTest
from src.applications.ls import Ls


class TestLs(ApplicationTest):

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "FolderHolder"
        self.file = "file1.txt"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.folders = {"folder1", "folder2", "folder3", ".folder4",
                        ".folder5"}
        for folder in self.folders:
            os.mkdir(os.path.join(self.folder, folder))

        with open(self.file, 'w'):
            pass

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)
        os.remove(self.file)

    def test_ls_zero_arg(self):
        os.chdir(self.folder)
        app_ls = Ls({"-a": False, "-r": False, "-s": False})
        app_ls.run([], self.out, [])
        os.chdir("..")
        result = self.out.popleft()
        folder = {"folder1", "folder2", "folder3"}
        for item in folder:
            self.assertIn(item, result)

    def test_ls_show_hidden(self):
        os.chdir(self.folder)
        app_ls = Ls({"-a": True, "-r": False, "-s": False})
        app_ls.run([], self.out, [])
        os.chdir("..")
        result = self.out.popleft()
        for item in self.folders:
            self.assertIn(item, result)

    def test_ls_s_flag(self):
        os.chdir(self.folder)
        app_ls = Ls({"-a": False, "-r": False, "-s": True})
        app_ls.run([], self.out, [])
        os.chdir("..")
        self.assertEqual(self.out.popleft(), "0folder1\t0folder2\t0folder3\n")

    def test_ls_r_flag(self):
        os.chdir(self.folder)
        app_ls = Ls({"-a": False, "-r": True, "-s": False})
        app_ls.run([], self.out, [])
        os.chdir("..")
        self.assertEqual(self.out.popleft(), "folder3\tfolder2\tfolder1\n")

    def test_ls_file(self):
        app_ls = Ls({"-a": False, "-r": False, "-s": False})
        self.assertRaises(NotADirectoryError, app_ls.run, [], self.out,
                          [self.file])

    def test_ls_help_message(self):
        self.assertEqual(Ls.help_message(self), "ls [-a -r -s] [directory]")


if __name__ == '__main__':
    unittest.main()
