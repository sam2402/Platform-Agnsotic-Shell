import unittest
from collections import deque

from applications.application import UnsafeApplication
from applications.ls import Ls


class TestUnsafe(unittest.TestCase):

    def setUp(self) -> None:
        self.out = deque()
        self.ls = Ls({"-a": False, "-r": False, "-s": False})
        self.unsafe_ls = UnsafeApplication(self.ls)

    def test_unsafe_help_message(self):
        self.assertEqual(self.unsafe_ls.help_message(), self.ls.help_message())

    def test_unsafe_exception(self):
        self.unsafe_ls.run([], self.out, ["fake_dir"])
        self.assertEquals(self.out, deque(["no such directory 'fake_dir'\n"]))
