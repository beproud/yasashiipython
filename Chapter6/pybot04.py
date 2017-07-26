# botの基本的なやりとりをファイルから読み込む
# これで、csvをいじればいろんな動作がさせられるよ

# open()のencodingの説明
# 

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

    if not response:
        response = '何ヲ言ッテルカ、ワカラナイ'
    print(response)

    if 'さようなら' in command:
        break
