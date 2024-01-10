# @Time    : 2024/1/10 AM11:44
# @Author  : kang
# @File    : day34_4.py
# @Desc    :
import time
from threading import Thread


def display(content):
    while True:
        print(content, end='', flush=True)
        time.sleep(0.1)


def main():
    Thread(target=display, args=('Ping', )).start()
    Thread(target=display, args=('Pong', )).start()


if __name__ == '__main__':
    main()