# @Time    : 2024/1/7 PM1:05
# @Author  : kang
# @File    : day19.py
# @Desc    :

from enum import Enum

from lesson19.Player import Player
from lesson19.Poker import Poker

poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)