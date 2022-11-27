import unittest
import src.applications.cat as cat
import os
import shutil
from collections import deque
from application_test import ApplicationTest, application_test
from parameterized import parameterized

class TestCat(ApplicationTest):

    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFiles"
        os.mkdir(self.folder)

        self.files = {
            "file1.txt": "this\nis\nfile\nnumber\none\n",
            "file2.txt": "and\nthis\nis\nthe\nsecond\nfile\n",
            "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles\n"
        }

        for filename, content in self.files.items():
            with open(os.path.join(self.folder, filename), "x") as f:
                f.write(content)

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)
    '''
    #def random_text(self, seed):

        #text = random_text(seed)
        #self.files[seed] = text

    #@paramatized([1], self.files[1])
    #def test_cat(self):

    '''

    def test_cat_valid_file(self):
        arg = os.path.join(self.folder,"file1.txt")
        cat.Cat.run(self,[],self.out,[arg])
        ans = self.files["file1.txt"].split()
        for i in range(len(self.out)):
            self.assertEqual(self.out.popleft(), ans[i] + "\n")

    #def test_cat_multiple_valid_files(self):
    #    arg, ans = [], []
    #    for filename, content in self.files.items():
    #        arg.append(os.path.join(self.folder,filename))
    #        ans.append(self.files[filename].split())

    def test_cat_stdin(self):
        text = "This is a default message to test cat function".split()
        cat.Cat.run(self, text, self.out, [])
        for i in range(len(text)):
            self.assertEqual(self.out.popleft(), text[i])

    def test_cat_help_message(self):
        self.assertEqual(cat.Cat.help_message(self), "cat [-n] [files...]")


if __name__ == '__main__':
    unittest.main()
