# @Time    : 2024/1/10 PM7:57
# @Author  : kang
# @File    : day36_2.py
# @Desc    :
def calc_average():
    total, counter = 0, 0
    avg_value = None
    while True:
        curr_value = yield avg_value
        total += curr_value
        counter += 1
        avg_value = total / counter


def main():
    obj = calc_average()
    # 生成器预激活
    obj.send(None)
    for _ in range(5):
        print(obj.send(float(input())))


if __name__ == '__main__':
    main()