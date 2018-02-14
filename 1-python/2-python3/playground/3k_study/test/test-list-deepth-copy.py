#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表的深浅copy
# 浅拷贝只能拷贝最外层，修改内层则原列表和新列表都会变化。
# 深拷贝是指将原列表完全克隆一份新的。
import copy

list1 = ['fruit', 'male', 1989, 'python', [2016, 2017], 'c']
list2 = list1.copy()  # 浅copy
list3 = copy.copy(list1)  # 浅copy，同list1.copy()效果相同
list4 = copy.deepcopy(list1)  # 深copy，会和list1占用同样大小的内存空间
list1[0] = '自由'
list1[4][0] = 2015
print(list1, '\n', list2, '\n', list3, '\n', list4)

# 列表的循环：逐个打印列表元素
list1 = ['fruit', 'male', 1989, 'python', [2016, 2017], 'c']
for i in list1:
    print(i)
