your_point = 76
if your_point >= 80:  # your_pointが80点以上か評価評価する式
    evaluation = 'Excellent!'  # your_pointが80点以上だった場合に処理されるプログラム
elif your_point >= 60:  # your_pointが80点未満だけど65点以上か評価する式
    evaluation = 'Good'
else:  # your_pointが65点未満の場合
    evaluation = 'Bad'
print('点数の評価は{}です。'.format(evaluation))
