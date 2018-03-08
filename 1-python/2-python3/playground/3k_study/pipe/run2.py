#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess
import sys
import threading


class LoopException(Exception):
    """循环异常自定义异常，此异常并不代表循环每一次都是非正常退出的"""

    def __init__(self, msg="LoopException"):
        self._msg = msg

    def __str__(self):
        return self._msg


class SwPipe:
    """
    与任意子进程通信管道类，可以进行管道交互通信
    """

    def __init__(self, command, func, exit_func, ready_func=None, shell=True, stdin=subprocess.PIPE,
                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, code="GBK"):
        """
        commande 命令
        func 正确输出反馈函数
        exitfunc 异常反馈函数
        readyfunc 当管道创建完毕时调用
        """
        self._thread = threading.Thread(target=self.__run, args=(command, shell, stdin, stdout, stderr, ready_func))
        self._code = code
        self._func = func
        self._exitfunc = exit_func
        self._flag = False
        self._CRFL = "\r\n"

    def __run(self, command, shell, stdin, stdout, stderr, ready_func):
        try:
            self._process = subprocess.Popen(command, shell=shell, stdin=stdin, stdout=stdout, stderr=stderr)
        except OSError as err:
            self._exitfunc(err)
        # fun = self._process.stdout.readline
        fun = self._process.stdout.readline
        self._flag = True
        if ready_func is None:
            threading.Thread(target=ready_func).start()  # 准备就绪
        while True:
            line = fun()rchermind

            # line = fun
            if not line:
                break
            try:
                tmp = line.decode(self._code)
            except UnicodeDecodeError:
                tmp = \
                    self._CRFL + "[PIPE_CODE_ERROR] <Code ERROR: UnicodeDecodeError>\n"
                + "[PIPE_CODE_ERROR] Now code is: " + self._code + self._CRFL
            self._func(self, tmp)

        self._flag = False
        self._exitfunc(LoopException("While Loop break"))  # 正常退出

    def write(self, msg):
        if self._flag:
            # 请注意一下这里的换行
            self._process.stdin.write((msg + self._CRFL).encode(self._code))
            self._process.stdin.flush()
            # sys.stdin.write(msg)#怎么说呢，无法直接用代码发送指令，只能默认的stdin
        else:
            raise LoopException("Shell pipe error from '_flag' not True!")  # 还未准备好就退出

    def start(self):
        """ 开始线程 """
        self._thread.start()

    def destroy(self):
        self.__process.stdout.close()
        self._thread.stop()
        del self


if __name__ == '__main__':  # 那么我们来开始使用它吧
    e = None


    # 输出反馈函数
    def event(cls, line):
        print("退出反馈函数")
        sys.stdout.write(line)


    # 退出反馈函数
    def exit(msg):
        print("退出反馈函数")
        print(msg)


    # 线程就绪反馈函数
    def ready():
        print("线程就绪反馈函数")
        e.write("ls")
        e.write("ping www.baidu.com")
        e.write("echo Hello!World 你好中国！你好世界！")
        e.write("exit")


    e = SwPipe("bash", event, exit, ready)
    e.start()
