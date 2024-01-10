# @Time    : 2024/1/10 PM3:14
# @Author  : kang
# @File    : day35_2.py
# @Desc    :

import os

print(f'PID: {os.getpid()}')
pid = os.fork()
if pid == 0:
    print(f'子进程 - PID: {os.getpid()}')
    print('Todo: 在子进程中执行的代码')
else:
    print(f'父进程 - PID: {os.getpid()}')
    print('Todo: 在父进程中执行的代码')
