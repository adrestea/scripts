#!/usr/bin/env python
# coding:utf-8
import os

import commands


def system(cmd):
    """
    1.fork一个子进程；
    2.在子进程中调用exec函数去执行命令；
    3.在父进程中调用wait（阻塞）去等待子进程结束。
    对于fork失败，system()函数返回-1
    返回运行shell命令状态，同时会在终端输出运行结果.在python中拿不到信息
    :return: 返回程序执行的状态, 成功或失败
    """
    # cmd = "cat abc.txt"
    return os.system(cmd)


def popen(cmd):
    # p = os.popen('ssh 10.3.16.121 ls')
    p = os.popen(cmd)
    x = p.read()
    print x
    p.close()
    return x


def subprocess_call(cmd):
    """
    代替os.system
    """
    # returnCode = subprocess.call('adb devices')
    returnCode = subprocess.call(cmd)
    print returnCode


def subprocess_(cmd, saved_file):
    """
    执行结果保存在文件
    :return:
    """
    # cmd = "adb shell ls /sdcard/ | findstr aa.png"
    # fhandle = open(r"e:\aa.txt", "w")
    fhandle = open(saved_file, "w")
    pipe = subprocess.Popen(cmd, shell=True, stdout=fhandle).stdout
    fhandle.close()


def subprocess_1(cmd):
    """
    执行结果使用管道输出
    """
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
    print pipe.read()


def subprocess(cmd):
    """
    同时返回结果和运行状态，commands模块:
    :param cmd:
    :return:
    """
    (exitstatus, outtext) = commands.getstatusoutput(cmd)
    print exitstatus, outtext
    # outtext = commands.getstatus(cmd)  # returns output of "ls -ld file"
    # print outtext


def ss(cmd):
    """
    方法就可以获得到返回值和输出：
    """
    (status, output) = commands.getstatusoutput(cmd)
    # (status, output) = commands.getstatusoutput('ssh hello.sh')
    print status, output


if __name__ == '__main__':
    subprocess("ls -l")
    pass
