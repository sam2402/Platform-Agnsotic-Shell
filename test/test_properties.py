import os
import random
import unittest
from collections import deque
from string import ascii_letters

from hypothesis import given, assume
from hypothesis.strategies import integers, lists, text

from applications.application import ApplicationError
from applications.cat import Cat
from applications.cd import Cd
from applications.cut import Cut
from applications.echo import Echo
from applications.find import Find
from applications.grep import Grep
from applications.head_tail import Head, Tail
from applications.ls import Ls
from applications.mkdir import Mkdir
from applications.rm import Rm
from applications.uniq import Uniq


class TestProperties(unittest.TestCase):
    def setUp(self):
        self.app_cat_n = Cat({"-n": True})

        self.app_cd = Cd()

        self.app_echo = Echo({"-n": False})
        self.app_echo_n = Echo({"-n": True})

        self.app_find = Find()

        self.app_grep = Grep({"-v": False, "-c": False})
        self.app_grep_i = Grep({"-v": True, "-c": False})

        self.app_ls = Ls()

        self.app_mkdir = Mkdir({"-p": False, "-v": False})

        self.app_rm = Rm({"-r": False, "-v": False, "-f": False})

        self.app_uniq_i = Uniq({"-i": True})

    @given(lists(text()))
    def test_cat_n_starts_with_line_no(self, inp: list[str]):
        out = deque()
        self.app_cat_n.run(inp, out, [])

        for i, line in enumerate(out):
            self.assertTrue(line.startswith(f"{i + 1} "))

    @given(text().filter(lambda s: "\0" not in s))
    def test_cd_raises_for_non_existent_dir(self, directory: str):
        assume(directory.isascii() and not os.path.isdir(directory))

        with self.assertRaises(ApplicationError):
            self.app_cd.run([], deque(), [directory])

    @given(lists(text(alphabet=ascii_letters)))
    def test_cut_b_1_len_returns_identical_string(self, inp: list[str]):
        for line in inp:
            out = deque()
            cut = Cut({"-b": f"1-{len(line)}"})
            cut.run([line], out, [])
            self.assertEqual(line, out.popleft().rstrip())

    @given(lists(text()))
    def test_echo_ends_with_newline(self, args: list[str]):
        assume(args)

        out = deque()
        self.app_echo.run([], out, args)
        self.assertTrue(out.popleft().endswith("\n"))

    @given(lists(text().filter(lambda s: "\n" not in s)))
    def test_echo_n_does_not_end_with_newline(self, args: list[str]):
        assume(args)

        out = deque()
        self.app_echo_n.run([], out, args)
        self.assertFalse(out.popleft().endswith("\n"))

    @given(text().filter(lambda s: "\0" not in s))
    def test_find_returns_empty_for_non_existent_path(self, path: str):
        assume(path.isascii() and not os.path.isdir(path))

        out = deque()
        self.app_find.run([], out, [path, "-name", ".*"])
        self.assertFalse(out)

    @given(lists(text()))
    def test_grep_finds_everything(self, lines: list[str]):
        out = deque()
        self.app_grep.run(lines, out, [".*"])

        self.assertEqual(len(out), len(lines))

        while out:
            self.assertEqual(out.popleft(), lines.pop(0))

    @given(lists(text()))
    def test_grep_i_finds_nothing(self, lines: list[str]):
        out = deque()
        self.app_grep_i.run(lines, out, [".*"])
        self.assertFalse(out)

    @given(integers(), lists(text()))
    def test_head_returns_correct_no_lines(self, n: int, lines: list[str]):
        assume(0 <= n <= len(lines))

        out = deque()
        head = Head({"-n": n, "-v": False})
        head.run(lines, out, [])

        self.assertEqual(len(out), n)

        while out:
            self.assertEqual(out.popleft(), lines.pop(0))

    @given(integers(), lists(text()))
    def test_tail_returns_correct_no_lines(self, n: int, lines: list[str]):
        assume(0 <= n <= len(lines))

        out = deque()
        tail = Tail({"-n": n, "-v": False})
        tail.run(lines, out, [])

        self.assertEqual(len(out), n)

        while out:
            self.assertEqual(out.pop(), lines.pop())

    @given(text().filter(lambda s: "\0" not in s))
    def test_ls_raises_for_non_existent_dir(self, directory: str):
        assume(directory.isascii() and not os.path.isdir(directory))

        with self.assertRaises(ApplicationError):
            self.app_cd.run([], deque(), [directory])

    @given(text(alphabet=ascii_letters), text(alphabet=ascii_letters))
    def test_mkdir_raises_for_nested_path_without_p(self, p1: str, p2: str):
        assume(p1 and p2 and not os.path.isdir(p1) and not os.path.exists(p1))

        with self.assertRaises(ApplicationError):
            self.app_mkdir.run([], deque(), [os.path.join(p1, p2)])

    @given(text().filter(lambda s: "\0" not in s))
    def test_rm_raises_for_non_existent_file(self, file: str):
        assume(file.isascii() and not os.path.exists(file))

        with self.assertRaises(ApplicationError):
            self.app_rm.run([], deque(), [file])

    @given(text(), integers(min_value=0, max_value=1000))
    def test_uniq_i_returns_single_entry(self, line: str, n: int):
        lines = [line, *[randomise_case(line) for _ in range(n)]]
        out = deque()
        self.app_uniq_i.run(lines, out, [])

        self.assertEqual(len(out), 1)
        self.assertEqual(out[0], line)


def randomise_case(s: str) -> str:
    return "".join(
        random.choice([c.lower, c.upper])() if c.isascii() else c for c in s
    )
