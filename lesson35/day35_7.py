# @Time    : 2024/1/10 PM4:19
# @Author  : kang
# @File    : day35_7.py
# @Desc    :

import time
from multiprocessing import Process, Queue


def sub_task(content, queue):
    counter = queue.get()
    while counter < 50:
        print(content, end='', flush=True)
        counter += 1
        queue.put(counter)
        time.sleep(0.01)
        counter = queue.get()


def main():
    queue = Queue()
    queue.put(0)
    p1 = Process(target=sub_task, args=('Ping', queue))
    p1.start()
    p2 = Process(target=sub_task, args=('Pong', queue))
    p2.start()
    while p1.is_alive() and p2.is_alive():
        pass
    queue.put(50)


if __name__ == '__main__':
    main()
