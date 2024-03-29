import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from applications.application import ApplicationError, ArgumentError
from applications.rm import Rm


class TestRm(ApplicationTest):

    application = Rm

    @staticmethod
    def make_dirs(*paths):
        path = os.path.join(os.getcwd(), *paths)
        os.mkdir(path)

    def setUp(self) -> None:
        self.out = deque()

        # Make main folder
        self.folder = "RmFolder"
        self.make_dirs(self.folder)

        # Add files to folder
        self.files = {"file1.txt", "file2.txt", "file3.txt"}
        for file in self.files:
            open(os.path.join(self.folder, file), 'w')

        # Add empty folder to main folder
        self.empty_folder = "empty_dir"
        self.make_dirs(self.folder, self.empty_folder)

        # Add folder with content to main folder
        self.nested_folder = "nested_dir"
        self.make_dirs(self.folder, self.nested_folder)
        for file in self.files:
            open(os.path.join(self.folder, self.nested_folder, file), 'w')

        self.nested_files = {
            "file1_nested.txt",
            "file2_nested.txt",
            "file3_nested.txt"
        }
        for file in self.files:
            open(os.path.join(self.folder, self.nested_folder, file), 'w')

        self.folder_contents = {
            *self.files,
            self.empty_folder,
            self.nested_folder
        }

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    @application_test({"-r": False, "-v": False, "-f": False})
    def test_zero_args(self, rm: Rm):
        with self.assertRaises(ArgumentError) as cm:
            rm.run([], self.out, [])
        self.assertEqual(
            str(cm.exception),
            "rm - supply at least one file path"
        )

    @application_test({"-r": False, "-v": False, "-f": False})
    def test_rm_normal(self, rm):
        file = os.path.join(self.folder, "file1.txt")
        rm.run([], self.out, [file])
        self.assertEqual(
            set(os.listdir(self.folder)),
            self.folder_contents-{"file1.txt"}
        )

    @application_test({"-r": True, "-v": False, "-f": False})
    def test_rm_recursive(self, rm):
        rm.run([], self.out, [os.path.join(self.folder, self.empty_folder)])
        self.assertEqual(
            set(os.listdir(self.folder)),
            self.folder_contents-{self.empty_folder}
        )

    @application_test({"-r": False, "-v": False, "-f": False})
    def test_rm_delete_dir_error(self, rm):
        with self.assertRaises(ApplicationError):
            rm.run([], self.out, [os.path.join(self.folder, "empty_dir")])

    @application_test({"-r": True, "-v": False, "-f": False})
    def test_rm_recursive_error(self, rm):
        with self.assertRaises(ApplicationError):
            rm.run([], self.out, [os.path.join(self.folder, "nested_dir")])

    @application_test({"-r": True, "-v": False, "-f": True})
    def test_rm_recursive_force(self, rm):
        rm.run([], self.out, [os.path.join(self.folder, "nested_dir")])
        self.assertEqual(
            set(os.listdir(self.folder)),
            self.folder_contents-{self.nested_folder}
        )

    @application_test({"-r": False, "-v": True, "-f": False})
    def test_rm_files_verbose(self, rm: Rm):
        rm.run([], self.out, list(map(
            lambda file: os.path.join(self.folder, file), self.files)))
        self.assertEqual(
            set(os.listdir(self.folder)),
            self.folder_contents-self.files
        )
        self.assertEqual(
            self.out,
            deque(map(
                lambda file:
                f"deleted file '{os.path.join(self.folder, file)}'\n",
                self.files
            ))
        )

    @application_test({"-r": True, "-v": True, "-f": False})
    def test_rm_dir_verbose(self, rm):
        rm.run([], self.out, [os.path.join(self.folder, self.empty_folder)])
        self.assertEqual(
            set(os.listdir(self.folder)),
            self.folder_contents-{self.empty_folder}
        )
        self.assertEqual(
            self.out,
            deque([
                f"deleted directory '"
                f"{os.path.join(self.folder, self.empty_folder)}'\n"
            ])
        )

    @application_test({"-h": True})
    def test_rm_help_message(self, rm):
        self.assertEqual(rm.help_message(),
                         "rm [-v -r -f] [directories/files...]")
