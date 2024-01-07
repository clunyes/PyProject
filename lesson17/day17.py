# @Time    : 2024/1/7 AM8:53
# @Author  : kang
# @File    : day17.py
# @Desc    :
from lesson17.Student import Student

stu1 = Student()
stu2 = Student()
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0>
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0

# 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)    # 学生正在玩游戏.
stu2.play()           # 学生正在玩游戏.