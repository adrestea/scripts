#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses

# 初始化curses
screen = curses.initscr()
# 设置不回显
# curses.noecho()
# 设置不需要按回车立即响应
# curses.cbreak()
# 开启键盘模式
screen.keypad(1)

# 阻塞模式读取0 非阻塞 1
screen.nodelay(0)

while True:
    char = screen.getch()
    # 根据得到的值进行操作
    # 无值为-1  其他为keyCode

# 恢复控制台默认设置（若不恢复，会导致即使程序结束退出了，控制台仍然是没有回显的）
# curses.nocbreak()
# screen.keypad(0)
# curses.echo()
# # 结束窗口
# curses.endwin()
