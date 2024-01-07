# @Time    : 2024/1/7 AM10:42
# @Author  : kang
# @File    : day18_3.py
# @Desc    :

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# 为Student对象动态添加sex属性
stu.sex = '男'
print("stu.sex==" + stu.sex)
