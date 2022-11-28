import os
import shutil
import unittest
from collections import deque
from application_test import ApplicationTest
from src.applications.application import ApplicationError
from src.applications.rm import Rm


class TestRm(ApplicationTest):
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "FolderHolder"
        self.dir_name = os.path.join(os.getcwd(), self.folder)
        os.mkdir(self.folder)
        self.folders = {"folder1", "folder2", "folder3"}
        for folder in self.folders:
            os.mkdir(os.path.join(self.folder, folder))

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)



    def test_rm_help_message(self):
        self.assertEqual(Rm.help_message(self),
                         "rm [-v -r -f] [directories/files...]")


if __name__ == '__main__':
    unittest.main()
