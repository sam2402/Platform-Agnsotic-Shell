
import unittest
import src.applications.ls as ls
import os
import shutil
from collections import deque

class TestLs(unittest.TestCase):

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
        ls.Ls.run(self, [], self.out, [])
        os.chdir("..")
        self.assertEqual(self.out.popleft(), "folder1\tfolder2\tfolder3\n")

    def test_ls_show_hidden(self):
        self.out = deque()
        os.chdir(self.folder)
        ls.Ls.run(self, [], self.out, ["-a"])
        os.chdir("..")
        result = self.out.popleft()
        for item in self.folders:
            self.assertIn(item, result)

    def test_ls_not_dir(self):
        self.out = deque()
        ls.Ls.run(self, [], self.out, [self.folder])
        self.assertEqual(self.out.popleft(), "folder1\tfolder2\tfolder3\n")

    def test_ls_help_message(self):
        self.assertEqual(ls.Ls.help_message(self), "ls [-a -r -s] [directory]")


if __name__ == '__main__':
    unittest.main()
