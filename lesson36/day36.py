# @Time    : 2024/1/10 PM7:24
# @Author  : kang
# @File    : day36.py
# @Desc    :
def fib(max_count):
    a, b = 0, 1
    for _ in range(max_count):
        a, b = b, a + b
        yield a


gen_obj = fib(20)
print(gen_obj)

for value in gen_obj:
    print(value)
