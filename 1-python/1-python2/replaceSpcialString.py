#!/usr/bin/python
#coding=utf-8

import os, sys

def replaceStr(file_path, str_old, str_new):
    f = open(file_path, "r+")
    for line in f:
        if str_old in line:
            print "replace---> " + str_old
            line = str.replace(line, str_old, str_new)
            f.write(line)
        f.flush()
    f.close()

if __name__ == '__main__':

    old = sys.argv[1]
    #new = sys.argv[2]
    #file = sys.argv[3]
    #file2 = sys.argv[3]
    #replaceStr("tmpfile", "            //byte[] data = intent.getByteArrayExtra(EXT_DATA_NAME);", "            byte[] data = intent.getByteArrayExtra(EXT_DATA_NAME);")
    #replaceStr("tmpfile", "            //byte[] data = intent.getByteArrayExtra(EXT_DATA_NAME);", "            ////byte[] data = intent.getByteArrayExtra(EXT_DATA_NAME);")
    replaceStr(old, "            //byte[] data = intent.getByteArrayExtra(EXT_DATA_NAME);", "            ////byte[] data = intent.getByteArrayExtra(EXT_DATA_NAME);")
    #os.remove(file)
    #os.rename(tmp_file, file2)
