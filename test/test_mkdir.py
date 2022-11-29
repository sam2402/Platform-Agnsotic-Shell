import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from applications.application import ApplicationError
from applications.mkdir import Mkdir


class TestMkdir(ApplicationTest):

    application = Mkdir

    def setUp(self) -> None:
        self.out = deque()
        self.already_exists = "dir1"
        os.mkdir(self.already_exists)

    def tearDown(self) -> None:
        shutil.rmtree(self.already_exists)

    @application_test({"-p": False, "-v": False})
    def test_mkdir_one_directory(self, mkdir):
        mkdir.run([], self.out, ["folder7"])
        self.assertIn("folder7", os.listdir())
        shutil.rmtree("folder7")

    @application_test({"-p": False, "-v": False})
    def test_mkdir_dir_already_exists(self, mkdir):
        with self.assertRaises(ApplicationError):
            mkdir.run([], self.out, [self.already_exists])

    @application_test({"-p": False, "-v": False})
    def test_mkdir_multiple_directories(self, mkdir):
        mkdir.run([], self.out, ["folder4", "folder5", "folder6"])
        dirs = {"folder4", "folder5", "folder6"}
        listdir = os.listdir()
        for directory in dirs:
            self.assertIn(directory, listdir)
        for dir in dirs:
            shutil.rmtree(dir)

    @application_test({"-p": False, "-v": True})
    def test_mkdir_verbose(self, mkdir):
        mkdir.run([], self.out, ["folder7"])
        self.assertIn("folder7", os.listdir())
        self.assertEqual(self.out.popleft(), "created directory folder7\n")
        shutil.rmtree("folder7")

    @application_test({"h": True})
    def test_mkdir_help_message(self, mkdir):
        self.assertEqual(mkdir.help_message(),
                         "mkdir [-v -p] [directories...]")
