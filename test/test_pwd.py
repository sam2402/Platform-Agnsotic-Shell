import os
from collections import deque

from application_test import ApplicationTest, application_test
from applications.pwd import Pwd


class TestPwd(ApplicationTest):

    application = Pwd

    @application_test(flags={"-P": False})
    def test_pwd_run(self, pwd):
        out = deque()
        pwd.run([], out, [])
        self.assertEqual(out.popleft(), os.getcwd() + "\n")

    @application_test(flags={"-P": True})
    def test_pwd_P_flag(self, pwd):
        out = deque()
        pwd.run([], out, [])
        non_symbolic_link = os.path.realpath(os.getcwd())
        self.assertEqual(out.popleft(), non_symbolic_link + "\n")

    @application_test(flags={"-h": True})
    def test_pwd_help_message(self, pwd):
        self.assertEqual(pwd.help_message(), "pwd [-P]")
