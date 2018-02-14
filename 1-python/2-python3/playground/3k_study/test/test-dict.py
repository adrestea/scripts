#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
·为什么dict查找速度这么快？
因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查找速度都非常快，不会随着字典大小的增加而变慢。dict就是第二种实现方式。
和list比较，dict有以下几个特点：
·无序
·查找和插入的速度极快，不会随着key的增加而变慢；
·需要占用大量的内存，内存浪费多。
而list相反：
·查找和插入的时间随着元素的增加而增加；
·占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
·dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
"""

# 创建空字典
dic = {}
print(type(dict))
# 直接赋值字典
dic = {'spam': 1, 'egg': 2, 'bar': 3}

# 通过关键字dict和关键字参数创建
dic = dict(spam=1, egg=2, bar=3)
print(dic)

# 通过二元组列表创建
list_d = [('spam', 1), ('egg', 2), ('bar', 3)]
dic = dict(list_d)
print(dic)

info = {
    'stu1': "Xiao Ming",
    'stu2': "Xiao Liang",
    'stu3': "Xiao Hong",
    'stu4': "Xiao Rui",
}
print(info)
# 修改
info['stu2'] = "Xiao Hu"
# 增加
info['stu5'] = "Xiao Fang"

# 删除
info.pop('stu2')
del info['stu1']
info.popitem()  # 随机删一个
print(info)
info.clear()  # 清空字典所有条目

# 查找
print('stu2' in info)  # 判断是否存在，存在则返回True，否则返回False
# print(info['stu1'])  # 如果一个key不存在，就报错，get不会，不存在只返回None

# dict.get(key, default=None)
# 返回指定键的值，如果值不在字典中返回default值
# 比较安全的查找方法
print(info.get('stu6'))

# 其他
print(info.values())  # 打印所有的值(即除了key)
print(info.keys())  # 打印所有的key
print(info.items())  # 把字典转化为列表

# dict.setdefault(key, default=None)
# 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
info.setdefault('class3', {'Xiao Rui', 15})
print(info)
info.setdefault('class1', {'Xiao Hong', 16})
print(info)

# 循环打印
for i in info:
    print(i, info[i])

for k, v in info.items():
    print(k, v)
# 多级字典嵌套及操作
info = {
    'class1': {
        'stu1': ["Xiao Ming", 16]
    },

    'class2': {
        'stu2': ["Xiao Liang", 17]
    }
}
info['class1']['stu1'][1] = 18
print(info)
# dict.fromkeys(seq[, val]))
# 创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
print(dict.fromkeys([6, 7, 8], 'test'))
c = dict.fromkeys([6, 7, 8], [1, {'name': 'frui'}])
c[6][1]['name'] = 'sorui'
print(c)
# update方法
info = {
    'stu1': "Xiao Ming",
    'stu2': "Xiao Liang",
    'stu3': "Xiao Hong",
    'stu4': "Xiao Rui",
}
b = {
    'stu1': "Xiao Dong",
    1: 3,
    2: 4
}
print(info)
info.update(b)
