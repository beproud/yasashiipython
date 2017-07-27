point_list = [75, 80, 91]  # リストを作成
total = 0  # 合計点数を計算するために0を代入して初期化
for point in point_list:
    total = total + point  # 点数を足していく
number_of_subjects = len(point_list)  # リストの長さを取得
average = total / number_of_subjects  # 合計点を全体の個数で割って平均点を出す
print('合計点は{}、平均点は{}です。'.format(total, average))  # 結果を表示
