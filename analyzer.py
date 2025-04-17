import re
from janome import tokenizer

def analyze(text):
    """
        形態素解析を行う関数

    :param text: str
        解析対象の文章

    :return: list[list[str]]
        形態素と品詞のペアを格納した多重リスト

    """
    t = tokenizer.Tokenizer()
    tokens = t.tokenize(text)
    result = [] # 解析結果の形態素と品詞を格納するリスト

    # リストからTokenオブジェクトを1つずつ取り出す
    for token in tokens:
        result.append([             # resultに追加する
            token.surface,          # 形態素を取得
            token.part_of_speech    # 品詞情報を取得
        ])

    return result


def keyword_check(part):
    """

        :param part: str
            形態素解析の品詞の部分
        :return: Match or None
            名詞であれば結果を格納したMatchオブジェクト、そうでなければNone

    """
    return re.match(
        '名詞,(一般|固有名詞|サ変接続|形容動詞語幹)',
        part
    )


def parse(text):
    t = tokenizer.Tokenizer()
    tokens = t.tokenize(text)
    result = []
    for token in tokens:
        result.append(token.surface)

    return result


def analyze_all(text):
    """
        形態素解析を行う関数

    :param text: str
        解析対象の文章

    :return: list[list[str]]
        形態素と品詞のペアを格納した多重リスト

    """
    t = tokenizer.Tokenizer()
    tokens = t.tokenize(text)
    result = [] # 解析結果の形態素と品詞を格納するリスト
    
    # リストからTokenオブジェクトを1つずつ取り出す
    for token in tokens:
        result.append([
            token.surface,          # 形態素を取得
            token.part_of_speech ,   # 品詞情報を取得
            token.infl_type,        # 活用型を取得
            token.base_form,         # 原型を取得
            token.reading,         # 読みを取得
        ])

    return result