import unittest

from applications.rm import Rm


class TestApplication(unittest.TestCase):

    def test_clean_args(self):
        cleaned = Rm.clean_args(["-r", "-v", "-x"])
        self.assertNotIn("-r", cleaned)
        self.assertNotIn("-v", cleaned)
        self.assertIn("-x", cleaned)
