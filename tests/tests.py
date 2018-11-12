import unittest
from MeCabOnigiri.tagger import get_dic_path, compile_user_dict, get_system_dic_list, get_tagger
from MeCabOnigiri.models import Token


class Test(unittest.TestCase):

    def test_1(self):
        tagger = get_tagger()
        word_list = tagger.parse_to_token('お金が欲しい')
        self.assertTrue(isinstance(word_list, list))

    def test_2(self):
        tagger = get_tagger()
        word_list = tagger.parse_to_token('お金が欲しい')
        self.assertListEqual(word_list, tagger.parse_to_token('お金が欲しい'))

    def test_hash(self):
        tagger = get_tagger()
        word_list = tagger.parse_to_token('お金が欲しい')
        hash(word_list[0])

    def test_set(self):
        tagger = get_tagger()
        set1 = set(tagger.parse_to_token('名誉が欲しい'))
        set2 = set(tagger.parse_to_token('お金が欲しいな'))
        self.assertSetEqual(set1 & set2,
                            {Token('が', '助詞'), Token('欲しい', '形容詞')})

    def test_get_dic_path(self):
        self.assertEqual(get_dic_path(), '/usr/local/lib/mecab/dic/mecab-ipadic-neologd')

    def test_default_dict_should_not_parse_user_settings(self):
        tagger = get_tagger()
        self.assertTrue(Token("ユーザ設定", "名詞") in tagger.parse_to_token("ユーザ設定が必要です。"))

    def test_add_user_dict(self):
        compile_user_dict('foo.csv', 'dic/foo.dic')

    def test_get_system_dict_list(self):
        self.assertListEqual(get_system_dic_list(), ['/usr/local/lib/mecab/dic/ipadic',
                                                     '/usr/local/lib/mecab/dic/mecab-ipadic-neologd'])
