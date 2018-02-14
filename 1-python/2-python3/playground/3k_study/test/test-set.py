#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 去重
list1 = [3, 2, 1, 4, 5, 6, 5, 4, 3, 2, 1]
print(list1, type(list1))

list1 = set(list1)
print(list1, type(list1))

list2 = set([4, 5, 6, 7, 8, 9])

# 交集
print(list1.intersection(list2))

# 并集
print(list1.union(list2))

# 差集
print(list1.difference(list2))
print(list2.difference(list1))

# 子集、父集
print(list1.issubset(list2))
print(list1.issuperset(list2))

list3 = set([4, 5, 6])
print(list3.issubset(list2))
print(list2.issuperset(list3))

# 对称差集
print(list1.symmetric_difference(list2))

# Return True if two sets have a null intersection
list4 = set([1, 2, 3])
print(list3.isdisjoint(list4))
# 交集
print(list1 & list2)
# union
print(list2 | list1)
# difference
print(list1 - list2)
# 对称差集
print(list1 ^ list2)
# 添加
list1.add(999)  # 添加一项
print(list1)
list1.update([66, 77, 88])  # 添加多项
print(list1)
print(list1.add(999))  # 猜猜打印什么？为什么

# 删除
list1.remove(999)
print(list1)

# remove and return arbitrary set element
print(list1.pop())

# Remove an element from a set if it is a member.If the element is not a member, do nothing.
print(list1.discard(888))
