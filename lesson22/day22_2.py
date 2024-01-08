# @Time    : 2024/1/8 AM11:22
# @Author  : kang
# @File    : day22_2.py
# @Desc    :


import json

with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)