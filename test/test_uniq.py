import os
from collections import deque

from application_test import ApplicationTest, application_test
from applications.uniq import Uniq


class TestUniq(ApplicationTest):

    application = Uniq

    def setUp(self) -> None:
        self.out = deque()
        self.app_uniq = Uniq({"-i": False})
        self.file_name = "file1.txt"
        self.text = "Uniq method test\nUniq method test\nUniQ MethoD TesT\n"

        with open(self.file_name, "x") as f:
            f.write(self.text)

    def tearDown(self) -> None:
        os.remove(self.file_name)

    @application_test({"-i": False})
    def test_uniq_no_options(self, uniq):
        uniq.run([], self.out, [self.file_name])
        ans = ["Uniq method test\n", "UniQ MethoD TesT\n"]
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i])

    @application_test({"-i": True})
    def test_uniq_case_insensitive(self, uniq):
        uniq.run([], self.out, [self.file_name])
        self.assertEqual(self.out.popleft(), "Uniq method test\n")

    @application_test({"-h": True})
    def test_uniq_help_message(self, uniq):
        self.assertEqual(uniq.help_message(), "uniq [-i] [file]")
