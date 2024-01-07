# @Time    : 2024/1/7 AM9:01
# @Author  : kang
# @File    : Student2.py
# @Desc    :

class Student2:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')
