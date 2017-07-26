# 条件分岐する
# 文字列の部分一致を使う(inの説明)

# pybot> こんにちは
# こんにちは
# pybot> pybotありがとう
# どういたしまして
# pybot> こんばんは
# 何を言ってるかわからない
# pybot> さようならpybot
# さようなら

while True:
    command = input('pybot> ')
    if 'こんにちは' in command:
        print('コンニチハ')
    elif 'ありがとう' in command:
        print('ドウイタシマシテ')
    elif 'さようなら' in command:
        print('サヨウナラ')
        break
    else:
        print('何ヲ言ッテルカ、ワカラナイ')
