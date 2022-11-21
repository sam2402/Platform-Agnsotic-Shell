import unittest
import src.applications.echo as echo

class TestEcho(unittest.TestCase):
    def test_echo_help_message(self):
        self.assertEqual(echo.Echo.help_message(self), "echo [args...]")

if __name__ == '__main__':
    unittest.main()
