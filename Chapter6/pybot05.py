# コマンドと数字の組み合わせで処理をする
# 干支コマンドの前フリ

# splitでいらないものを _ で捨てている説明

# pybot> 平成 2000
# 2000年は平成12年です
# pybot> 平成 1980
# 1980年は平成ではありません

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
        heisei, year_str = command.split()
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = '西暦{}年ハ、平成{}年デス'.format(year, heisei_year)
        else:
            response = '西暦{}年ハ、平成デハアリマセン'.format(year)

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
