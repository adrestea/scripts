#!/usr/bin/env python
#coding:utf-8       #设置python文件的编码为utf-8，这样就可以写入中文注释

import os.path
import time
import exceptions
class TypeError (Exception):
    pass

def __getLastModifyTime(file_path):
    if not os.path.exists(file_path):
        raise TypeError()
    mtime = time.ctime(os.path.getmtime(file_path))
    ctime = time.ctime(os.path.getctime(file_path))
#    print "Last modified : %s, last created time: %s" % (mtime, ctime)
    return mtime

def getLastModifyFileName():
    path = os.getcwd()
    if os.path.exists(path):
        files = os.listdir(path)
        file_list = {}
        lasted_ctime_file = ""
        for file in files:
            file_list[__getLastModifyTime(file)] = file
        print file_list.keys().sort()

#        if len(file_list):
#            lasted_ctime_file = file_list[0]
#        print ("Files\t---> %s\nLasted\t---> %s") % (file_list, lasted_ctime_file)
#        return lasted_ctime_file
        print file_list

if __name__ == '__main__':
    getLastModifyFileName()