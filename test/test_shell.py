import contextlib
import sys
import unittest
from collections import deque
import io

from shell import evaluate, run_shell, handle_input, ShellError


class TestShell(unittest.TestCase):

    def test_run_shell_throws_for_invalid_arg(self):
        argv = sys.argv

        sys.argv = ["", "-k"]
        with self.assertRaises(ShellError):
            run_shell()

        sys.argv = argv

    def test_run_shell_correct_argument(self):
        argv = sys.argv

        sys.argv = ["", "-c", "echo foo"]
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            run_shell()

        self.assertEqual("foo\n", out.getvalue())

        sys.argv = argv

    def test_shell_no_args(self):
        argv = sys.argv
        sys.argv = []
        run_shell()
        sys.argv = argv

    def test_evaluate(self):
        out = deque()
        evaluate("echo foo bar", out)
        self.assertEqual(out.popleft(), "foo bar\n")

    def test_handle_input_empty(self):
        handle_input("")

    def test_handle_input_non_empty(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            handle_input("echo hello")

        self.assertEqual("hello\n", out.getvalue())

    def test_handle_input_catches_argument_error(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            handle_input("find")

        self.assertTrue(err.getvalue().startswith("argument error: find"))

    def test_handle_input_catches_application_error(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            handle_input("<doesnotexist.txt echo")

        exp = "application error: input file 'doesnotexist.txt' does not exist"
        self.assertEqual(err.getvalue(), exp + "\n")

    def test_handle_input_catches_parsing_error(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            handle_input("||")

        self.assertTrue(err.getvalue().startswith(
            "parsing error: improperly formatted subcommand"
        ))

        exp = "application error: input file 'doesnotexist.txt' does not exist"
        self.assertEqual(err.getvalue(), exp + "\n")

    def test_handle_input_catches_parsing_error(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            handle_input("||")

        self.assertTrue(err.getvalue().startswith(
            "parsing error: improperly formatted subcommand"
        ))
