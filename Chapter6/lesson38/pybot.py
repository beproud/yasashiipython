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

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
