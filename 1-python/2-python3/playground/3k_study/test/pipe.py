#!/usr/bin/python
# -*- coding: UTF-8 -*-

# with Popen(["echo", "a"], stdout=PIPE) as proc:
#     print(proc.stdout.read())


from subprocess import *

p = Popen('ls', shell=False, stdin=PIPE, stdout=PIPE)


def run():
    global p
    while True:
        line = p.stdout.readline()
        if len(line) == 3:  # 空则跳出
            break
        print(">>>>>>", line.decode("GBK"))
    print("look up!!! EXIT ===")  # 跳出


run()

# w = threading.Thread(target=run)
# w.start()

# while True:
#     val = input("i:")
#     p.stdin.write(val.encode("GBK"))
#     p.stdin.flush()
# p.stdin.write("echo HELLW_WORLD!\r\n".encode("GBK"))
#
# # time.sleep(1)  # 延迟是因为等待一下线程就绪
# #
# # p.stdin.write("2".encode("GBK"))
# # p.stdin.flush()
# # time.sleep(1)  # 延迟是因为等待一下线程就绪
# # p.stdin.write("exit\r\n".encode("GBK"))
# # p.stdin.flush()


# import os
# import sys
#
# print
# "The child will write text to a pipe and "
# print
# "the parent will read the text written by child..."
#
# # file descriptors r, w for reading and writing
# r, w = os.pipe()
#
# processid = os.fork()
# if processid:
#     # This is the parent process
#     # Closes file descriptor w
#     os.close(w)
#     r = os.fdopen(r)
#     print
#     "Parent reading"
#     str = r.read()
#     print
#     "text =", str
#     sys.exit(0)
# else:
#     # This is the child process
#     os.close(r)
#     w = os.fdopen(w, 'w')
#     print
#     "Child writing"
#     w.write("Text written by child...")
#     w.close()
#     print
#     "Child closing"
#     sys.exit(0)
