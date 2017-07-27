year_str = input('あなたの生まれ年を西暦4桁で入力してください: ')
year = int(year_str)  # 入力された値をint型へ変換
number_of_eto = (year + 8) % 12  # 計算結果を変数へ代入
print(number_of_eto)  # 結果を表示
