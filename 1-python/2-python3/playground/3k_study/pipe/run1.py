#!/usr/bin/env python
# encoding: utf-8

from subprocess import *
import threading
import time

p = Popen('bash', shell=True, stdin=PIPE, stdout=PIPE)


def run():
    global p
    while True:
        line = p.stdout.readline()
        if not line:  # 空则跳出
            break
        print(">>>>>>", line.decode("GBK"))

    print("look up!!! EXIT ===")  # 跳出


w = threading.Thread(target=run)

p.stdin.write("echo gao HELLW_WORLD!\r\n".encode("GBK"))
p.stdin.flush()
time.sleep(1)  # 延迟是因为等待一下线程就绪
p.stdin.write("exit\r\n".encode("GBK"))
p.stdin.flush()

w.start()