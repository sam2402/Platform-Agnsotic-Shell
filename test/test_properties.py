import os
import unittest
from collections import deque
from typing import List

from hypothesis import given, assume
from hypothesis.strategies import lists, text

import string

from applications.application import ApplicationError
from applications.cat import Cat
from applications.cd import Cd
from applications.cut import Cut
from applications.echo import Echo


class TestProperties(unittest.TestCase):
    def setUp(self):
        self.app_cat_n = Cat({"-n": True})

        self.app_cd = Cd()

        self.app_echo = Echo({"-n": False})
        self.app_echo_n = Echo({"-n": True})

    @given(lists(text()))
    def test_cat_n_starts_with_line_no(self, inp: List[str]):
        out = deque()
        self.app_cat_n.run(inp, out, [])

        for i, line in enumerate(out):
            self.assertTrue(line.startswith(f"{i + 1} "))

    @given(text())
    def test_cd_raises_for_non_existent_dir(self, directory: str):
        assume(directory.isalnum() and not os.path.isdir(directory))

        with self.assertRaises(ApplicationError):
            self.app_cd.run([], deque(), [directory])

    @given(lists(text(alphabet=string.ascii_letters)))
    def test_cut_b_1_len_returns_identical_string(self, inp: List[str]):
        for line in inp:
            out = deque()
            cut = Cut({"-b": f"1-{len(line)}"})
            cut.run([line], out, [])
            self.assertEqual(line, out.popleft().rstrip())

    @given(lists(text()))
    def test_echo_ends_with_newline(self, args: List[str]):
        assume(args)

        out = deque()
        self.app_echo.run([], out, args)
        self.assertTrue(out.popleft().endswith("\n"))

    @given(lists(text().filter(lambda s: "\n" not in s)))
    def test_echo_n_does_not_end_with_newline(self, args: List[str]):
        assume(args)

        out = deque()
        self.app_echo_n.run([], out, args)
        self.assertFalse(out.popleft().endswith("\n"))
