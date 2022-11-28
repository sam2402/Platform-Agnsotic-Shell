import os
import unittest
from collections import deque

from application_test import ApplicationTest
from src.applications.pwd import Pwd


class TestPwd(ApplicationTest):
    def setUp(self) -> None:
        self.app_pwd = Pwd({"-P": False})

    def test_pwd_run(self):
        self.out = deque()
        self.app_pwd.run([], self.out, [])
        self.assertEqual(self.out.popleft(), os.getcwd() + "\n")

    def test_pwd_P_flag(self):
        self.out = deque()
        app_pwd_p = Pwd({"-P": True})
        app_pwd_p.run([], self.out, [])
        non_symbolic_link = os.path.realpath(os.getcwd())
        self.assertEqual(self.out.popleft(), non_symbolic_link + "\n")

    def test_pwd_help_message(self):
        self.assertEqual(Pwd.help_message(self), "pwd [-P]")


if __name__ == '__main__':
    unittest.main()
