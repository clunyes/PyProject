# @Time    : 2024/1/5 PM3:10
# @Author  : kang
# @File    : day11_3.py
# @Desc    : 不可变集合


set1 = {'Java', 'Python', 'Go', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Objective-C', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))    # False
print(set1.isdisjoint(set3))    # True


set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))
print(set1 & set2)    # frozenset({1, 3, 5})
print(set1 | set2)    # frozenset({1, 2, 3, 4, 5, 7})
print(set1 - set2)    # frozenset({7})
print(set1 < set2)    # False