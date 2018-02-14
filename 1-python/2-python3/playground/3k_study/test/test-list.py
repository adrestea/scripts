#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list内元素的数据类型可以不同,也可以是另外一个list
list1 = ['frui', 'male', 1989, 'python', [2016, 2017], 'c']
list2 = ['']
print("1==>", list1)

# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符，如下所示：
print("2==>", list1[:])
print("3==>", list1[0], list1[1])
print("4==>", list1[-1], list1[-2])
print("5==>", list1[0:3])  # 切片,此操作顾头不顾尾
print("6==>", list1[:3])
print("7==>", list1[-3:])  # 切片，从后向前数索引，也只能从左往右切片，同样是顾头不顾尾。（这样会无法取到最后一个元素，思考怎么办？）
print("8==>", list1[0:-1:2])  # 按步长切片
print("8==>", list1[0::2])  # 按步长切片
print("9==>", list1[::2])  # 按步长切片
print("9==>", list1[1::2])  # 按步长切片

list1.append("linux")  # 在列表末尾追加元素
list1.insert(1, "linux")  # 直接把元素插入的指定位置
list1[0] = "jay"  # （改）直接替换某个位置元素

# delete
list1.pop()  # 删除list末尾的元素
list1.pop(1)  # 删除指定位置的元素
del list1[0]
list1.remove("python")  # 此种方法和前两种的区别是什么？

print("10==>", list1)
print("11==>", list1.index(1989))  # 查找已知元素的索引
print("12==>", list1[list1.index(1989)])

print("13==>", list1.count(1989))  # 打印某元素在列表中的数量
list1.clear()  # 清除整个列表
list1.reverse()  # 反转整个列表
list1.sort()  # 排序 按ASCII码顺序排序,若元素中有list类型，则无法排序，为什么？

list2 = [1, 2, 3, 4]
list1.extend(list2)  # 列表合并
print("14==>", list1)
del list2  # 删除整个变量
