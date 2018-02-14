#!/usr/bin/env python
#coding:utf-8       #设置python文件的编码为utf-8，这样就可以写入中文注释
'''
'''
import time
#######################################################
def getCurrentTime():
    now = int(time.time()) #获得当前时间时间戳
    timeArray = time.localtime(now)
    return time.strftime("%H:%M:%S_%Y-%m-%d", timeArray)