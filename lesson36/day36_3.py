# @Time    : 2024/1/10 PM7:58
# @Author  : kang
# @File    : day36_3.py
# @Desc    :
import time


def display(num):
    time.sleep(1)
    print(num)


def main():
    start = time.time()
    for i in range(1, 10):
        display(i)
    end = time.time()
    print(f'{end - start:.3f}秒')


if __name__ == '__main__':
    main()