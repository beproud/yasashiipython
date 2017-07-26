# 組み込み関数を使う
# input(), int(), print(), open() も組み込み関数だよ
# http://docs.python.jp/3.5/library/functions.html
# 同じ仕組みで max, min も作れるよ

# スライス(num_str_list[1:])の説明

# pybot> 長さ supercalifragilisticexpialidocious
# 文字列ノ長サハ 34 文字デス
# pybot> 長さ 寿限無寿限無五劫の擦り切れ海砂利水魚の水行末雲来末風来末食う寝るところに住むところやぶら小路のぶら小路パイポパイポパイポのシューリンガン、シューリンガンのグーリンダイ、グーリンダイのポンポコピーのポンポコナーの長久命の長助
# 文字列ノ長サハ 111 文字デス


def heisei_command(command):
    heisei, year_str = command.split()
    year = int(year_str)
    if year >= 1989:
        heisei_year = year - 1988
        response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
    else:
        response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    return response


def len_command(command):
    cmd, text = command.split(maxsplit=1)
    length = len(text)
    response = '文字列ノ長サハ {} 文字デス'.format(length)
    return response


bot_dict = {}
command_file = open('pybot04.csv', encoding='utf-8')
raw_data = command_file.read()
for line in raw_data.splitlines():
    key, response = line.split(',')
    bot_dict[key] = response

while True:
    command = input('pybot> ')
    response = ""
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            break

    if '平成' in command:
        response = heisei_command(command)
    if '長さ' in command:
        response = len_command(command)

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
