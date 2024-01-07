# @Time    : 2024/1/7 AM9:01
# @Author  : kang
# @File    : day17_2.py
# @Desc    :
from lesson17.Student2 import Student2

# 由于初始化方法除了self之外还有两个参数
# 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student2('骆昊', 40)
stu2 = Student2('王大锤', 15)
stu1.study('Python程序设计')    # 骆昊正在学习Python程序设计.
stu2.play()                    # 王大锤正在玩游戏.