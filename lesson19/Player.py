# @Time    : 2024/1/7 PM1:21
# @Author  : kang
# @File    : Player.py
# @Desc    :

class Player:
    """玩家"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()