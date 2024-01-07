# @Time    : 2024/1/7 PM1:20
# @Author  : kang
# @File    : Poker.py
# @Desc    :


import random

from lesson19.Card import Card
from lesson19.Suite import Suite


class Poker:
    """扑克"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机乱序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)