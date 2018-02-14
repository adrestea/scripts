#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import sys
import os


def usage():
    print('''
        Usage： original-file replaced-string new-file
        example:
           python3 replace-special-strings.py /home/alex/Desktop/test/abc.txt "{'bcd':'aaa','fg':'eee'}" /home/alex/Desktop/test/aaa.txt
    ''')


def main():
    len_argv = len(sys.argv)

    if len_argv < 3:
        usage()
    if len_argv > 4:
        usage()
    else:
        if not os.path.isfile(sys.argv[1]):
            print('文件不存在')
            sys.exit()
        if os.path.exists(sys.argv[3]):
            os.remove(sys.argv[3])
        s_file = open(sys.argv[1], 'r+')
        d_file = open(sys.argv[1] + '.tmp', 'w')
        str_dict = eval(sys.argv[2])
        for line in s_file.readlines():
            for key in str_dict:
                line = line.replace(key, str_dict[key])
            d_file.writelines(line)
        s_file.close()
        d_file.close()

        os.rename(sys.argv[1] + '.tmp', sys.argv[3])


if __name__ == "__main__":
    main()
