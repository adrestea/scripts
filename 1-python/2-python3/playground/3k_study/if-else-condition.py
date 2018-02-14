#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# FileName: if-else-condition.py


age = int(input("Please input the age:\n"))
if age < 0:
    print("input error!")
elif age >10:
    print("长寿啊！")
else:
    print("age is %d"%age)