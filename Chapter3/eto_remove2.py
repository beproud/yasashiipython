eto_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
eto_name = eto_list[1]  # eto_listの1番目の要素をeto_nameへ代入する
print('remove()実行前の干支リスト1番は', eto_name, 'です。')
eto_list.remove('丑')  # 丑を削除する
eto_name = eto_list[1]  # eto_listの1番目の要素をeto_nameへ代入する
print('remove()実行後の干支リスト1番は', eto_name, 'です。')
