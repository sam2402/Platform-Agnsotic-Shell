import unittest

from flagging import Flag, FlagConfiguration


class TestApplicationFactory(unittest.TestCase):

    def setUp(self):

        self.flags = [
            Flag("-v", bool, "--verbose"),
            Flag("-x", int, argument_count=3)
        ]
        self.flag_config = FlagConfiguration(self.flags)

    def test_flag_to_string(self):
        self.assertEqual(str(self.flags[0]), "-v")

    def test_flag_config_to_string(self):
        self.assertEqual(str(self.flag_config), "['-h', '-v', '-x']")

    def test_get_non_existent_flag(self):
        with self.assertRaises(KeyError):
            self.flag_config["-y"]
