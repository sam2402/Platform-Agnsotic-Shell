import unittest
import src.applications.cat as cat
import os
import shutil
from collections import deque

class TestCat(unittest.TestCase):
    '''
    def setUp(self) -> None:
        self.out = deque()
        self.folder = "TestFiles"
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)

        # self.files = {
        #     "file1.txt": "this\nis\nfile\nnumber\none",
        #     "file2.txt": "and\nthis\nis\nthe\nsecond\nfile",
        #     "file3.txt": "third\nfile\nto\ntest\nmultiple\nfiles"
        # }

    def tearDown(self) -> None:
        shutil.rmtree(self.folder)

    #def random_text(self, seed):

        #text = random_text(seed)
        #self.files[seed] = text

    #@paramatized([1], self.files[1])
    #def test_cat(self):





    def test_cat_help_message(self):
        self.assertEqual(cat.Cat.help_message(self), "cat [files...]")

    '''
if __name__ == '__main__':
    unittest.main()
