year_str = input('あなたの生まれ年を西暦4桁で入力してください: ')
year = int(year_str)
number_of_eto = (year + 8) % 12
print(number_of_eto)
