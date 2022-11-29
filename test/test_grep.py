import os
import shutil
from collections import deque

from application_test import ApplicationTest, application_test
from applications.application import ArgumentError, ApplicationError
from applications.grep import Grep


class TestGrep(ApplicationTest):

    application = Grep

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFiles"
        os.mkdir(self.folder)

        self.files = {
            "file1.txt": "This is the first line\nand this is the second "
                         "line\ngrep method",
            "file2.txt": "multiple files have been created\nto test grep"
                         "\nworks on multiple lines",
            "file3.txt": "and the output\nshould be the file name and line"
        }

        for filename, content in self.files.items():
            with open(os.path.join(self.folder, filename), "x") as f:
                f.write(content)

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    @application_test()
    def test_grep_no_args(self, grep):
        with self.assertRaises(ArgumentError):
            grep.run([], self.out, [])

    @application_test(flags={"-v": False, "-c": False})
    def test_grep_invalid_args(self, grep):
        arg = os.path.join(self.folder, "file1.txt")
        with self.assertRaises(ApplicationError):
            grep.run([], self.out, ["66s\\55a", arg])

    @application_test(flags={"-v": False, "-c": False})
    def test_grep_one_valid_arg(self, grep):
        arg = os.path.join(self.folder, "file1.txt")
        grep.run([], self.out, ["second", arg])
        self.assertEqual(self.out.popleft(), "and this is the second line\n")

    @application_test(flags={"-v": False, "-c": False})
    def test_grep_multiple_valid_arg(self, grep):
        arg = os.path.join(self.folder, "file1.txt")
        grep.run([], self.out, ["line", arg])
        ans = ["This is the first line\n", "and this is the second line\n"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i])

    @application_test(flags={"-v": False, "-c": False})
    def test_grep_multiple_files(self, grep):
        arg = []
        for file_name in self.files:
            arg.append(os.path.join(self.folder, file_name))
        grep.run([], self.out, ["line", arg[0], arg[1], arg[2]])
        ans = [arg[0] + ":This is the first line\n",
               arg[0] + ":and this is the second line\n",
               arg[1] + ":works on multiple lines",
               arg[2] + ":should be the file name and line"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i])

    @application_test(flags={"-v": True, "-c": False})
    def test_grep_invert(self, grep):
        inp = ["tinker", "tailor", "soldier", "spy"]
        grep.run(inp, self.out, ["t.*r"])
        self.assertListEqual(list(self.out), ["soldier", "spy"])

    @application_test(flags={"-v": False, "-c": True})
    def test_group_colour(self, grep):
        inp = ["rum gum ram bar rim bat"]
        c, r = grep.highlight_colour, grep.reset_colour
        expected = f"{c}rum{r} gum {c}ram{r} bar {c}rim{r} bat"
        grep.run(inp, self.out, ["r.m"])
        self.assertEqual(self.out.popleft(), expected)

    @application_test({"-h": True})
    def test_grep_help_message(self, grep):
        self.assertEqual(
            grep.help_message(),
            "grep [-v -c] <pcre> [files...]"
        )
