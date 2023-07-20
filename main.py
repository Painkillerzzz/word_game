import argparse
import json
import random
from langdetect import detect
# import streamlit as st


def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    2. -c 为可选参数，表示输入文章题目
    3. -l 为可选参数，表示是否限制语言
    4. -s 为可选参数，表示输入输出路径

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-c", "--choose", help="文章题目")
    parser.add_argument("-l", "--language", action="store_true", help="语言限制")
    parser.add_argument("-s", "--save", help="输出路径")

    parsers = parser.parse_args()
    return parsers


def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            alldata = json.load(f)
    except IOError:
        args.file = input("Error: 文件不存在！请输入正确的文件名: ")
        return read_articles(args.file)
    else:
        return alldata


def select_article(choose):
    """
        读取所选文章

        :param choose: 所选文章名

        :return: 一个字典，所选文章
    """
    crt_article = random.choice(articles)
    if choose is not None:
        flag = False
        for i in articles:
            if i["title"] == choose:
                crt_article = i
                flag = True
                break
        if not flag:
            crt_article = random.choice(articles)
            print("Warning: 文章未找到，已开启随机模式。")
    return crt_article


def input_change(lang, crt_hint, crt_keys):
    change = input(f"请输入{crt_hint}：")
    try:
        input_lang = detect(change)
    except Exception:
        print("Error: 语言检测失败，请重试！")
        input_change(lang, crt_hint, crt_keys)
    else:
        if input_lang == lang:
            crt_keys.append(change)
        else:
            print(f"Error: 语言不正确({input_lang})，请重试({lang})！")
            input_change(lang, crt_hint, crt_keys)


def get_inputs(lang, hints):
    """
    获取用户输入

    :param lang: 使用语言
    :param hints: 提示信息

    :return: 用户输入的单词
    """

    all_keys = []
    for hint in hints:
        if args.language:
            input_change(lang, hint, all_keys)
        else:
            all_keys.append(input(f"请输入{hint}："))
    return all_keys


def replace(crt_article, keys):
    """
    替换文章内容

    :param crt_article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for index in range(len(keys)):
        crt_article = crt_article.replace("{{%s}}" % str(index + 1), keys[index])

    return crt_article


def output_data(out_article):
    if args.save is None:
        print(out_article)
    else:
        with open(args.save, 'w') as f:
            f.write(out_article)


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]
    article = select_article(args.choose)

    print(article["article"])
    keys = get_inputs(data["language"], article["hints"])
    article = replace(article["article"], keys)
    output_data(article)
