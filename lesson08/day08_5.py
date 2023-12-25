# @Time    : 2023/12/25 PM4:45
# @Author  : kang
# @File    : day08_5.py
# @Desc    :嵌套的列表可以用来表示表格或数学上的矩阵


scores = [[0] * 3 for _ in range(5)]
scores[0][0] = 95
print(scores)
# [[95, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]