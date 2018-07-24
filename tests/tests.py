import unittest
from MeCabOnigiri import get_word_list


class Test(unittest.TestCase):

    def test_1(self):
        word_list = get_word_list('お金が欲しい')
        self.assertTrue(isinstance(word_list, list))

    def test_2(self):
        self.assertListEqual(get_word_list('お金が欲しい'), get_word_list('お金が欲しい'))
