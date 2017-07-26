# とりあえずコマンドを入力してそのまま返すbot

# while は新しい要素なので説明する
# Trueについても説明する
# Ctrl+C でぬけることも説明
# Ctrl+C が何をしているものなのか、読み方、アクションの仕方も説明

# コードの意味として「コマンド」って何という話をする
# botに命令をして、それに対して応答を返してもらうみたいなイメージかな

# pybot> こんにちは
# こんにちは
# pybot> こんばんは
# こんばんは
# pybot> Ctrl+C

while True:
    command = input('pybot> ')
    print(command)
