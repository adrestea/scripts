# !/usr/bin/env python
# coding: utf-8

"""
该部分是使用evdev获取事件节点, 通过节点文件能够准确的获取键盘事件
注意: 1.该脚本需要root权限来执行

input子系统详解
        http://blog.csdn.net/ylyuanlu/article/details/6704744
使用Python获取/dev/input目录下event对应的设备
        http://blog.csdn.net/huangxiongbiao/article/details/46983489
Linux下使用Python捕获键盘输入
        http://blog.csdn.net/huangxiongbiao/article/details/47063299
"""
from evdev import InputDevice
from select import select


def detectInputKey():
    """
    event3 :鼠标事件
    event2 :键盘事件
    """
    dev = InputDevice('/dev/input/event2')
    while True:
        select([dev], [], [])
        for event in dev.read():
            print "code:%s value:%s" % (event.code, event.value)
            if (event.value == 1 or event.value == 0) and event.code != 0:
                print "Key: %s Status: %s" % (event.code, "pressed" if event.value else "release")


if __name__ == '__main__':
    detectInputKey()
