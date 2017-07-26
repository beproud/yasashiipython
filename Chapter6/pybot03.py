# botの基本的なやりとりを辞書にする

# 「さようなら」が入っていたら強制的に抜ける
# 辞書の順番が不定であることを説明する
# 空文字の説明をする。もしくはNoneにするか
# `if not responce` がなんのかも説明する

bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'さようなら': 'サヨウナラ',
    }

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
