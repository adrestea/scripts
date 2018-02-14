#!/usr/bin/evn python3
# -*- coding: utf-8 -*-


'''
args: 要解析的命令行参数列表。
options: 以字符串的格式定义，options后的冒号(:)表示该选项必须有附加的参数，不带冒号表示该选项不附加参数。
long_options: 以列表的格式定义，long_options 后的等号(=)表示如果设置该选项，必须有附加的参数，否则就不附加参数。
该方法返回值由两个元素组成: 第一个是 (option, value) 元组的列表。 第二个是参数列表，包含那些没有'-'或'--'的参数
'''

import sys
import getopt


def usage():
    print('test.py -i <inputfile> =o <outputfile>')


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--ofile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print("输入的文件为：", inputfile)
    print("输出的文件为：", outputfile)


if __name__ == '__main__':
    main(sys.argv[1:])
