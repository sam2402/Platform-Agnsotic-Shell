import unittest

from applications.application import (
    ApplicationError,
    ArgumentError
)
from applications.head_tail import Head
from flagging import Flag, FlagConfiguration
from application_factory import ApplicationFactory


class TestApplicationFactory(unittest.TestCase):

    def test_get_application_with_one_flag_param(self):
        app = ApplicationFactory().get_application(
            ["head", "-n", "3", "file.txt"]
        )
        self.assertIsInstance(app, Head)
        self.assertEqual(app.flags["-n"], 3)

    def test_parse_flags_with_multiple_flag_params(self):
        flag_dict = ApplicationFactory()._parse_flags(
            FlagConfiguration([
                Flag("-x", int, argument_count=2)
            ]),
            ["-x", "1", "2"]
        )
        self.assertEqual(flag_dict, {"-h": False, "-x": [1, 2]})

    def test_parse_flags_with_missing_flag(self):
        with self.assertRaises(SyntaxError):
            ApplicationFactory()._parse_flags(
                FlagConfiguration([
                    Flag("-x", int, argument_count=2)
                ]),
                ["-n", "1", "2"]
            )

    def test_parse_flags_with_missing_optional_flag_with_default_value(self):
        flag_dict = ApplicationFactory()._parse_flags(
            FlagConfiguration([
                Flag(
                    "-x",
                    int,
                    argument_count=2,
                    default_value=[24, 2],
                    is_optional=True
                )
            ]),
            []
        )
        self.assertEqual(flag_dict, {"-h": False, "-x": [24, 2]})

    def test_parse_flags_with_missing_optional_bool_flag(self):
        flag_dict = ApplicationFactory()._parse_flags(
            FlagConfiguration([
                Flag("-x", bool, is_optional=True)
            ]),
            []
        )
        self.assertEqual(flag_dict, {"-h": False, "-x": False})

    def test_parse_flags_with_missing_default_val(self):
        flag_dict = ApplicationFactory()._parse_flags(
            FlagConfiguration([
                Flag("-x", str, is_optional=True)
            ]),
            []
        )
        self.assertEqual(flag_dict, {"-h": False})

    def test_get_application_with_fake_name(self):
        with self.assertRaises(ApplicationError):
            ApplicationFactory().get_application(["not_real"])

    def test_get_application_with_invalid_argument_types(self):
        with self.assertRaises(ArgumentError):
            ApplicationFactory().get_application(["head", "-n", "NaN", "file"])

    def test_get_application_with_invalid_argument_count(self):
        with self.assertRaises(ArgumentError):
            ApplicationFactory().get_application(["head", "-n"])
