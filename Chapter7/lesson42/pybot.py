from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command


def len_command(command):
    cmd, text = command.split()
    length = len(text)
    response = '文字列ノ長サハ {} 文字デス'.format(length)
    return response


def heisei_command(command):
    heisei, year_str = command.split()
    year = int(year_str)
    if year >= 1989:
        heisei_year = year - 1988
        response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
    else:
        response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    return response


command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
lines = raw_data.splitlines()

bot_dict = {}
for line in lines:
    word_list = line.split(',')
    key = word_list[0]
    response = word_list[1]
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
    if '干支' in command:
        response = eto_command(command)
    if '選ぶ' in command:
        response = choice_command(command)
    if 'さいころ' in command:
        response = dice_command()
    if '今日' in command:
        response = today_command()
    if '現在' in command:
        response = now_command()
    if '曜日' in command:
        response = weekday_command(command)

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
