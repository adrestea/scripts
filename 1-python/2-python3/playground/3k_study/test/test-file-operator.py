#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""

# f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。
# f = open("file_test", 'r+', encoding='utf-8')  # 文件句柄
f = open("file_test", 'w', encoding='utf-8')  # 文件句柄
f.write("i couldn't make the color match today\n")
print(f.write("i don't know what else to say"))
f.close

# f.read()为了读取一个文件的内容，调用f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
# size是一个可选的数字类型的参数。 当size被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
f = open("file_test", 'r', encoding='utf-8')  # 文件句柄
data = f.read()
data2 = f.read()
print(data)
print('---data2---', data2)  # 思考输出是否和data一致

# f.readlines()会从文件中读取单独的一行。换行符为'\n'。
# f.readline()如果返回一个空字符串, 说明已经已经读取到最后一行。下面循环方式会把文件内容全部读到内存当中
f = open("file_test", 'r', encoding='utf-8')
for index, line in enumerate(f.readlines()):
    if index == 4:
        print('---------------')
        continue
    print(line.strip())

# 高效的循环
f = open("file_test", 'r', encoding='utf-8')
count = 0
for line in f:
    if count == 4:
        print('----------')
        count += 1
        continue
    print(line)
    count += 1

# f.tell()返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
# f.seek()如果要改变文件当前的位置, 可以使用f.seek(offset, from_what)函数。
# from_what的值, 如果是0表示开头, 如果是1表示当前位置, 2表示文件的结尾，例如：
# seek(x, 0) ： 从起始位置即文件首行首字符开始移动x个字符
# seek(x, 1) ： 表示从当前位置往后移动x个字符
# seek(-x, 2)：表示从文件的结尾往前移动x个字符
# from_what值为默认为0，即文件开头。下面给出一个完整的例子：
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)
print(f.readline())

# 其它函数
print(f.encoding)
print(f.fileno())
print(f.name)  # 打印文件名
print(f.flush())  # 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
print(f.truncate(10))  # 截取文件，截取的字节通过size指定，默认为当前文件位置。
# 进度条

import sys
import time

for i in range(20):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(0.2)
# 文件修改
f = open("file_test", "r", encoding="utf-8")
f_new = open("file_test.bak", "w", encoding="utf-8")

for line in f:
    if "what else to say" in line:
        line = line.replace("what else to say", "what else to fuck")
    f_new.write(line)
f.close()
f_new.close()

# with语句为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open("file_test", "r", encoding="utf-8") as f, \
        open("file_test", "r", encoding="utf-8") as f2:
    for line in f:
        print(line)
# 如此方式，当with代码块执行完毕时，内不会自动关闭并释放文件资源。在Python2.7后，with又支持同时对多个文件的上下文进行管理。

# 字符编码与转码需知: 在python2默认编码是ASCII, python3里默认是unicode, unicode分为utf - 32(占4个字节), utf - 16(占两个字节)，utf - 8(占1 - 4个字节)，
# 所以utf - 16就是现在最常用的unicode版本，不过在文件里存的还是utf - 8，因为utf8省空间在py3中encode,
# 在转码的同时还会把string变成bytes类型，decode在解码的同时还会把bytes变回string -*- coding:gbk -*-

s = "你好"
print(s.encode("gbk"))
print(s.encode("utf-8"))
print(s.encode("utf-8").decode("utf-8").encode("gb2312").decode("gb2312"))
