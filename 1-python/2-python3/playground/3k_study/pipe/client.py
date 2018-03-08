#!/usr/bin/env python3
# encoding: utf-8
# named pipe Client

import os

write_path = "/tmp/server_in.pipe"
read_path = "/tmp/server_out.pipe"

counter = 1

f = os.open(write_path, os.O_SYNC | os.O_CREAT | os.O_RDWR)
print
"Client open f", f

rf = None

while True:
    # Client发送请求
    req = "%s " % counter
    len_send = os.write(f, req)
    print
    "request", req, len_send

    counter += 1

    if rf is None:
        # *要点1：在这里第一次打开read_path，实际这里的open是一个阻塞操作
        # 打开的时机很重要。如果在程序刚开始，没发送请求就打开read_path，肯定会阻塞住
        rf = os.open(read_path, os.O_RDONLY)
        print
        "client opened rf", rf

        # 接收Server回应
    s = os.read(rf, 1024)
    if len(s) == 0:
        # 一般来说，是管道被意外关闭了，比如Server退出了
        break

    print
    "received", s

    # 这个例子里没有sleep，客户端以最高速度发送数据，可以观察执行效果

os.close(f)
os.close(rf)
