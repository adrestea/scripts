#!/usr/bin/env python
# coding: utf-8

import os


def showDevice():
    deviceFilePath = '/sys/class/input/'  # 源目录
    os.chdir(deviceFilePath)
    for i in os.listdir(os.getcwd()):
        namePath = deviceFilePath + i + '/device/name'
        if os.path.isfile(namePath):
            print "Name: %s Device: %s" % (i, file(namePath).read())


if __name__ == "__main__":
    showDevice()
