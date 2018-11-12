import MeCab
import subprocess
from .models import Token


class TaggerOption:
    default = ''
    wakati = '-Owakati'
    yomi = '-Oyomi'
    chasen = '-Ochasen'
    dump = '-Odump'


def get_tagger(format=TaggerOption.default, user_dic=''):
    dic_path = get_dic_path()
    user_dic = user_dic or '/Users/akiya/Projects/MeCabOnigiri/foo.dic'
    tagger = MeCab.Tagger(f'{format} -d {dic_path} -u {user_dic}')
    # https://qiita.com/kasajei/items/0805b433f363f1dba785
    tagger.parse("")

    if format == TaggerOption.default:
        return DefaultTagger(tagger)
    return DefaultTagger(tagger)


class DefaultTagger:

    def __init__(self, tagger):
        self.tagger = tagger

    def parse_to_token(self, text):
        words = []
        node = self.tagger.parseToNode(text)

        # 最初は捨てる (BOS/EOS)
        node = node.next
        while node:
            splitted = node.feature.split(',')
            word = node.surface
            part_of_speech = splitted[0]
            if part_of_speech == 'BOS/EOS':
                break
            token = Token(word=word, part_of_speech=part_of_speech)
            words.append(token)
            node = node.next

        return words


def get_system_dic_list():
    system_dic_root = str(subprocess.check_output('mecab-config --dicdir', shell=True))[2:-3]
    shell_output = str(subprocess.check_output(f'ls {system_dic_root}', shell=True))[2:-3]
    print(shell_output)
    dic_name_list = shell_output.split('\\n')
    return [f'{system_dic_root}/{dic_name}' for dic_name in dic_name_list]


def get_dic_path():
    system_dic_list = get_system_dic_list()
    neologd = 'mecab-ipadic-neologd'
    for system_dic in system_dic_list:
        if neologd in system_dic:
            return system_dic
    else:
        return system_dic_list[0]


def get_mecab_dict_cmd_root():
    return str(subprocess.check_output('mecab-config --libexecdir'))


def compile_user_dict(dict_file_name: str, dest_file_path: str):
    mecab_dict_index_path = '/usr/local/Cellar/mecab/0.996/libexec/mecab/mecab-dict-index'
    shell = f'{mecab_dict_index_path} -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -u dic/foo.dic -f utf-8 -t utf-8 foo.csv'
    return str(subprocess.check_output(shell, shell=True))
