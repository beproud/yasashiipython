# 平成コマンドを関数にする
# def, return


def heisei_command(command):
    heisei, year_str = command.split()
    year = int(year_str)
    if year >= 1989:
        heisei_year = year - 1988
        response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
    else:
        response = '西暦{}年ハ、平成デハアリマセン'.format(year)
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

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
