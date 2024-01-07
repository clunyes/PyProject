# @Time    : 2024/1/7 PM1:10
# @Author  : kang
# @File    : Suite.py
# @Desc    :
from enum import Enum


class Suite(Enum):
    """花色(枚举)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)