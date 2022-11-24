import unittest
import src.applications.mkdir as mkdir
import os
import shutil
from collections import deque

class TestMkdir(unittest.TestCase):


    def test_mkdir_help_message(self):
        self.assertEqual(mkdir.Mkdir.help_message(self), "mkdir [directories...]")


if __name__ == '__main__':
    unittest.main()
