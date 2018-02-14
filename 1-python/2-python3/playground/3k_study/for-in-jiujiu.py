#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
九九乘法表
"""

line = 1
while line < 10:
    j = 1
    while j <= line:
        print("%d*%d=%d" % (j, line, j * line), end="\t")
        j += 1
    print("\n")
    line += 1
