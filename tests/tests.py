import unittest
from MeCabOnigiri import get_word_list
from MeCabOnigiri.tagger import get_dic_path
from MeCabOnigiri.models import Token


class Test(unittest.TestCase):

    def test_1(self):
        word_list = get_word_list('お金が欲しい')
        self.assertTrue(isinstance(word_list, list))

    def test_2(self):
        self.assertListEqual(get_word_list('お金が欲しい'), get_word_list('お金が欲しい'))

    def test_3(self):
        get_word_list('紙幣が何かわからない')

    def test_hash(self):
        hash(get_word_list('お金が欲しい')[0])

    def test_set(self):
        set1 = set(get_word_list('名誉が欲しい'))
        set2 = set(get_word_list('お金が欲しいな'))
        self.assertSetEqual(set1 & set2,
                            {Token('が', '助詞'), Token('欲しい', '形容詞')})

    def test_get_dic_path(self):
        self.assertEqual(get_dic_path(), '/usr/local/lib/mecab/dic/mecab-ipadic-neologd')
