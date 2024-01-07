# @Time    : 2024/1/7 AM10:36
# @Author  : kang
# @File    : day18.py
# @Desc    :

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu.__name)
