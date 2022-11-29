import os
import shutil
from collections import deque

from application_test import ApplicationTest
from applications.application import ApplicationError
from applications.mkdir import Mkdir


class TestMkdir(ApplicationTest):

    def setUp(self) -> None:
        self.out = deque()
        self.app_mkdir = Mkdir({"-p": False, "-v": False})
        self.already_exists = "dir1"
        os.mkdir(self.already_exists)

    def tearDown(self) -> None:
        shutil.rmtree(self.already_exists)

    def test_mkdir_one_directory(self):
        self.app_mkdir.run([], self.out, ["folder7"])
        self.assertIn("folder7", os.listdir())
        shutil.rmtree("folder7")

    def test_mkdir_dir_already_exists(self):
        self.assertRaises(ApplicationError, self.app_mkdir.run, [], self.out,
                          [self.already_exists])

    def test_mkdir_multiple_directories(self):
        self.app_mkdir.run([], self.out, ["folder4", "folder5", "folder6"])
        dirs = {"folder4", "folder5", "folder6"}
        listdir = os.listdir()
        for directory in dirs:
            self.assertIn(directory, listdir)
        for dir in dirs:
            shutil.rmtree(dir)

    def test_mkdir_verbose(self):
        app_mkdir_v = Mkdir({"-p": False, "-v": True})
        app_mkdir_v.run([], self.out, ["folder7"])
        self.assertIn("folder7", os.listdir())
        self.assertEqual(self.out.popleft(), "created directory folder7\n")
        shutil.rmtree("folder7")

    def test_mkdir_help_message(self):
        self.assertEqual(Mkdir.help_message(self),
                         "mkdir [-v -p] [directories...]")
