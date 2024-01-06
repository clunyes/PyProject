# @Time    : 2024/1/6 AM9:37
# @Author  : kang
# @File    : day15_3.py
# @Desc    :

def calc(*args):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    return result


# print(calc(a=1, b=2, c=3))

def calc(*args, **kwargs):
    result = 0
    for arg in args:
        if type(arg) in (int, float):
            result += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            result += value
    return result


print(calc())                  # 0
print(calc(1, 2, 3))           # 6
print(calc(a=1, b=2, c=3))     # 6
print(calc(1, 2, c=3, d=4))    # 10
