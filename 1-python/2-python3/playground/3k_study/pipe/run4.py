#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import signal
import threading
import time
import sys

'''
该代码实现:
1. 线程1朝管道里面写信息, 线程1通过管道读取.
2. 使用signal信号能够立即中断(關鍵點:设置signal同时不用join方法而deni而使用while pass.
'''

pipe_name = 'pipe_test'


def child():
    pipeout = os.open(pipe_name, os.O_WRONLY)
    counter = 0
    while True:
        print(counter)
        val = input("input number:")
        print('Parent %d got at %s' % (os.getpid(), time.time()))
        os.write(pipeout, bytes('Number %s\n' % val, encoding="utf8"))


def parent():
    pipein = open(pipe_name, 'r')
    while True:
        line = pipein.readline()[:-1]
        print('Parent %d got "%s" at %s' % (os.getpid(), line, time.time()))


def quit(signum, frame):
    print('You choose to stop me.')
    try:
        if os.path.exists(pipe_name):
            os.remove(pipe_name)
    except Exception:
        pass
    sys.exit()


if __name__ == '__main__':
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        if not os.path.exists(pipe_name):
            os.mkfifo(pipe_name)
        pid = os.fork()
        print(pid)
        if pid != 0:
            a = threading.Thread(target=child)
            b = threading.Thread(target=parent)
            a.setDaemon(True)
            a.start()
            b.setDaemon(True)
            b.start()

        while True:
            pass
    except Exception as exc:
        print(exc)
