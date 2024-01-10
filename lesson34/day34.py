# @Time    : 2024/1/9 PM5:09
# @Author  : kang
# @File    : day34.py
# @Desc    :
import random
import time


def download(*, filename):
    start = time.time()
    print(f'开始下载 {filename}.')
    time.sleep(random.randint(3, 6))
    print(f'{filename} 下载完成.')
    end = time.time()
    print(f'下载耗时: {end - start:.3f}秒.')


def main():
    start = time.time()
    download(filename='Python从入门到住院.pdf')
    download(filename='MySQL从删库到跑路.avi')
    download(filename='Linux从精通到放弃.mp4')
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')


if __name__ == '__main__':
    main()
