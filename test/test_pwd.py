import unittest
import src.applications.pwd as pwd
import os
from collections import deque


class TestPwd(unittest.TestCase):

    def test_pwd_run(self):
        self.out = deque()
        pwd.Pwd.run(self, [], self.out, [])
        self.assertEqual(self.out.popleft(), os.getcwd()+"\n")

    def test_pwd_help_message(self):
        self.assertEqual(pwd.Pwd.help_message(self), "pwd")


if __name__ == '__main__':
    unittest.main()
