#!/usr/bin/env python3
# -*- coding: utf-8 -*-

u = u'中文'  # 显示指定unicode类型对象u
print u
print u.encode('gb2312')  # 以gb2312编码对unicode对像进行编码
print u.encode('gbk')  # 以gbk编码对unicode对像进行编码
print u.encode('utf-8')  # 以utf-8编码对unicode对像进行编码
print u.decode('gb2312')  # 以gb2312编码对字符串str进行解码，以获取unicode
# u2 = str.decode('utf-8')  # 如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
