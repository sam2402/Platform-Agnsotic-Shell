import tempfile
import unittest

from parser import execute_command, ParsingError


class TestParser(unittest.TestCase):

    # def test_raises_for_empty_input(self):
    #    with self.assertRaises(ParsingError):
    #        execute_command("")

    def test_double_pipe(self):
        out = execute_command("echo abc | cat | cat")
        expected = ["abc\n"]
        self.assertEqual(out, expected)

    def test_double_input_redirection_raises(self):
        with self.assertRaises(ParsingError):
            execute_command("<in1.txt <in2.txt echo hello world")

    def test_double_output_redirection_raises(self):
        with self.assertRaises(ParsingError):
            execute_command("echo hello world >out1.txt >out2.txt")

    def test_single_quoted(self):
        out = execute_command("echo \'foo bar\'")
        expected = ["foo bar\n"]
        self.assertEqual(out, expected)

    def test_single_quoted_invalid(self):
        with self.assertRaises(ParsingError):
            execute_command("echo '\n'")

    def test_double_quoted(self):
        out = execute_command("echo \"foo bar\"")
        expected = ["foo bar\n"]
        self.assertEqual(out, expected)

    def test_double_quoted_invalid(self):
        with self.assertRaises(ParsingError):
            execute_command("echo \"\n'\"")

    def test_back_quoted(self):
        out = execute_command("echo `echo foo bar`")
        expected = ["foo bar\n"]
        self.assertEqual(out, expected)

    def test_back_quoted_invalid(self):
        with self.assertRaises(ParsingError):
            execute_command("```")

    def test_back_quoted_within_double_quotes(self):
        out = execute_command("echo \"foo `echo bar`\"")
        expected = ["foo bar\n"]
        self.assertEqual(out, expected)

    def test_arg_splitting(self):
        with tempfile.NamedTemporaryFile(mode="a") as tmp:
            tmp.write("Hello World\n")
            tmp.write("Goodbye World\n")
            tmp.flush()

            out = execute_command(f"echo `cat {tmp.name}`")
            expected = ["Hello World Goodbye World\n"]
            self.assertEqual(out, expected)


if __name__ == '__main__':
    unittest.main()
