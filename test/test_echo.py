import unittest
import src.applications.echo as echo
from collections import deque

class TestEcho(unittest.TestCase):

    def test_echo_run(self):
        self.out = deque()
        echo.Echo.run(self, [], self.out, ["foo", "bar"])
        self.assertEqual(self.out.popleft(),"foo bar" + "\n")

    def test_echo_help_message(self):
        self.assertEqual(echo.Echo.help_message(self), "echo [args...]")

if __name__ == '__main__':
    unittest.main()
