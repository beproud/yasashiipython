year_str = input('あなたの生まれ年を西暦4桁で入力してください: ')
year = int(year_str)
number_of_eto = (year + 8) % 12
print('あなたの干支の順番は', number_of_eto, '番です。')
