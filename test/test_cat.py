import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from applications.cat import Cat


class TestCat(ApplicationTest):

    application = Cat

    def setUp(self):
        self.out = deque()
        self.folder = "TestFiles"
        os.mkdir(self.folder)

        self.files = {
            "file1.txt": "this\nis\nfile\nnumber\none\n",
            "file2.txt": "and\nthis\nis\nthe\nsecond\nfile\n",
            "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles\n"
        }

        for filename, content in self.files.items():
            with open(os.path.join(self.folder, filename), "x") as f:
                f.write(content)

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    @application_test(flags={"-n": False})
    def test_cat_valid_file(self, cat):
        arg = os.path.join(self.folder, "file1.txt")
        cat.run([], self.out, [arg])
        ans = self.files["file1.txt"].split()
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i] + "\n")

    @application_test(flags={"-n": False})
    def test_cat_stdin(self, cat):
        text = "This is a default message to test cat function".split()
        cat.run(text, self.out, [])
        for i in range(len(text)):
            self.assertEqual(self.out.popleft(), text[i])

    @application_test(flags={"-n": False})
    def test_cat_help_message(self, cat):
        self.assertEqual(cat.help_message(), "cat [-n] [files...]")
