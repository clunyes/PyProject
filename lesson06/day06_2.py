# @Time    : 2023/12/25 PM3:37
# @Author  : kang
# @File    : day06_2.py

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i * j}', end='\t')
    print()