import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from src.applications.application import ApplicationError
from src.applications.wc import Wc


class TestWc(ApplicationTest):

    application = Wc

    def setUp(self):
        self.out = deque()
        self.folder = "TestFiles"
        os.mkdir(self.folder)

        self.files = {
            "file1.txt": "this\nis\nfile\nnumber\none\n",
            "file2.txt": "and\nthis\nis\nthe\nsecond\nfile\n",
            "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles"
        }

        for filename, content in self.files.items():
            with open(os.path.join(self.folder, filename), "x") as f:
                f.write(content)

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    @application_test(flags={"-w": True, "-l": False, "-b": False})
    def test_wc_invalid_file(self, wc):
        with self.assertRaises(ApplicationError):
            wc.run([], self.out, "file5.txt")

    @application_test(flags={"-w": True, "-l": False, "-b": False})
    def test_wc_w_valid_file(self, wc):
        arg = os.path.join(self.folder, "file1.txt")
        wc.run([], self.out, [arg])
        self.assertEqual(self.out.popleft(), "5\n")

    @application_test(flags={"-w": False, "-l": True, "-b": False})
    def test_wc_l_valid_file(self, wc):
        arg = os.path.join(self.folder, "file3.txt")
        wc.run([], self.out, [arg])
        self.assertEqual(self.out.popleft(), "6\n")

    @application_test(flags={"-w": False, "-l": False, "-b": True})
    def test_wc_b_valid_file(self, wc):
        arg = os.path.join(self.folder, "file2.txt")
        wc.run([], self.out, [arg])
        self.assertEqual(self.out.popleft(), "28\n")

    @application_test(flags={"-w": True, "-l": False, "-b": False})
    def test_wc_stdin(self, wc):
        text = "This is a default message to test wc function".split(" ")
        wc.run(text, self.out, [])
        self.assertEqual(self.out.popleft(), "9\n")

    @application_test()
    def test_cat_help_message(self, wc):
        self.assertEqual(wc.help_message(), "wc [-w -l -b] [files...]")
