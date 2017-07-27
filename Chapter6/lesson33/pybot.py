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
