import tempfile
import unittest

import parser


class TestCommand(unittest.TestCase):

    def test_help(self):
        command = parser.parse_command("echo -h")
        out = command.execute()

        self.assertEqual(len(out), 1)
        self.assertTrue(out.pop(), "echo [-n] [args...]\n")

    def test_in_out(self):
        with tempfile.NamedTemporaryFile() as in_file, \
             tempfile.NamedTemporaryFile() as out_file:
            command = parser.parse_command(
                f"echo Hello <{in_file.name} >{out_file.name}"
            )
            out = command.execute()
            self.assertFalse(out)
