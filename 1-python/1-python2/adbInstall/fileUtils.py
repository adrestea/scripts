#!/usr/bin/env python
#coding:utf-8       #设置python文件的编码为utf-8，这样就可以写入中文注释
'''
'''
import datetime
import os
import hashlib
import re

def GetFileMd5(file_name):
    '''
    Get the fileName md5 value
    '''
    startTime = datetime.datetime.now()
    if not os.path.isfile(file_name):
        return
    myHash = hashlib.md5()
    f = file(file_name,'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myHash.update(b)
    f.close()
    endTime = datetime.datetime.now()
    print '运行时间：%ds'%((endTime-startTime).seconds)
    return myHash.hexdigest()

def getStrMd5(str):
    '''
    Get the string MD5SUM
    '''
    hash = hashlib.md5()
    hash.update(str)
    return hash.hexdigest()

def openUTFFile(file_path):
    fh = open(file_path)
    return fh.read().decode('utf-8')

if __name__ == '__main__':
    file_str = openUTFFile(u'/media/New_Disk/Project/code/Squid-nosv-master-0418/LINUX/android/vendor/fujitsu/apps/IrisUnlock/AndroidManifest.xml')
    '''
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.fujitsu.mobile_phone.irisunlock"
    android:versionCode="1"
    '''
    m1 = re.match(r".*", file_str)
    if m1:
        print m1.group(0)
    else:
        print 'not match'
    #if m1:
    #    print("find : %s" % m1.group())