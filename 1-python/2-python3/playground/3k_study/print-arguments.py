#!/usr/bin/python3
# -*- coding: utf-8 -*-
# filename:print-arguments.py

import sys


def doMain():
    print("命令行参数为：")
    for param in sys.argv:
        print(param, end=" ,")

    print("\n")
    for row in sys.path: print(repr(row))


if __name__ == '__main__':
    doMain()
