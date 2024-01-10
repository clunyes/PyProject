# @Time    : 2024/1/10 AM11:50
# @Author  : kang
# @File    : day34_7.py
# @Desc    :
import time
from concurrent.futures import ThreadPoolExecutor
from threading import RLock


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = RLock()

    def deposit(self, money):
        # 获得锁
        self.lock.acquire()
        try:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
        finally:
            # 释放锁
            self.lock.release()


def main():
    """主函数"""
    account = Account()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(100):
            pool.submit(account.deposit, 1)
    print(account.balance)


if __name__ == '__main__':
    main()