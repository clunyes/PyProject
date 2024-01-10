# @Time    : 2024/1/5 PM4:10
# @Author  : kang
# @File    : day12_5.py
# @Desc    : 字典使用

sentence = input('请输入一段话: ')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
for key, value in counter.items():
    print(f'字母{key}出现了{value}次.')
