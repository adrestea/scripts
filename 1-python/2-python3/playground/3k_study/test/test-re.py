#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# print(re.match('www.', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
#
# line = "Cats are smarter than dogs"
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")

key_words = u"《一念永恒》正文卷"

# matchObj = re.match(u"》正文卷", key_words, re.U)
matchObj = re.match("《\S*》正文卷", key_words)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
