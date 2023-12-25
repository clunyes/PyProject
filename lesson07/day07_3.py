# @Time    : 2023/12/25 PM4:04
# @Author  : kang
# @File    : day07_3.py
# @Desc    : 斐波那契数列。


a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)