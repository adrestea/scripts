#/usr/bin/python
#coding-utf-8
import subprocess
import os

if __name__ == '__main__':
    res_File = "/home/user/DeskTop/res/all_nospace_1"
    cmd = "find /home/user/py/UI_Specs -type f |grep -i "
    f = open(res_File, "r")
    for line in f:
        line_num = os.popen(cmd + line.strip('\n')).read()
        print(line.strip('\n') + "  ------------>")
        print(line_num+ "\n")

