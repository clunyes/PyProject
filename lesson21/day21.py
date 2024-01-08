# @Time    : 2024/1/7 PM1:31
# @Author  : kang
# @File    : day21.py
# @Desc    : 文件读写


file = open('致橡树.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end='')
file.close()

file = open('致橡树.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()