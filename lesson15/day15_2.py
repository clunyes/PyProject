# @Time    : 2024/1/6 AM9:28
# @Author  : kang
# @File    : day15_2.py
# @Desc    : 函数进阶2

def is_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b
"""
调用函数时，如果希望函数的调用者必须以参数名=参数值的方式传参，
可以用命名关键字参数（keyword-only argument）取代位置参数。所谓命名关键字参数，是在函数的参数列表中，写在*之后的参数，代码如下所示。
"""

# TypeError: is_triangle() takes 0 positional arguments but 3 were given
# print(is_triangle(3, 4, 5))
# 传参时必须使用“参数名=参数值”的方式，位置不重要
print(is_triangle(a=3, b=4, c=5))
print(is_triangle(c=5, b=4, a=3))
