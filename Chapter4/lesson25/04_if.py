your_point = input('点数をカンマ区切りで入力してください: ')  # 点数をカンマ区切りで入力
point_list = your_point.split(',')  # カンマ区切りで点数データをリストに格納
total = 0

for point in point_list:  # 点数の合計を求める
    total += int(point)

# 評価基準となる値を求める
subject_number = len(point_list)
excellent = subject_number * 100 * 0.8
good = subject_number * 100 * 0.65
# if、elif、elseで判定
if total >= excellent:
    evaluation = 'Excellent!'
elif total >= good:
    evaluation = 'Good'
else:
    evaluation = 'Bad'

print('点数の評価は{}です。'.format(evaluation))  # 結果を表示
