#!/usr/bin/env python
#coding:utf-8       #设置python文件的编码为utf-8，这样就可以写入中文注释
'''
'''

import sys
import getopt
import os
import commands
from statistic.utils import config
import path
import fileUtils
import timUtils

CONFIG_FILE={
    "Settings":"/system/priv-a/Settings/Settings.apk",
    "tmpDir":"/home/alex"}

def getRootRemount():
    return runCommand(True, "adb root", "adb remount")

def runCommand(logs, *cmd):
    length = len(cmd)
    cmds = ''
    if 0 == length:
        cmds = cmd[0]
    else:
        cmds = cmd[0]
        for i in range(1, length):
            cmds = cmds +" && "+ cmd[i]
    (status, output) = commands.getstatusoutput(cmds)
    res = "ok."
    if status == 1:
        res = "nok."
    print "------------------------>", cmds, " [", res, "]"
    if logs:
        print output
    return (status == 0, output)

#######################################################
def saveAPK():
    pass

#######################################################
def getAPKName(fileName):
    return fileName + timUtils.getCurrentTime()

#######################################################
def store(fileName):
    if fileName in CONFIG_FILE:
        fileMd5 = fileUtils.GetFileMd5(getAPKName(fileName))
    else:
        pass

#######################################################
def usage():
    '''
    -h, --help
        display help information
    -s, --store
        store the apk
    -r, --restore
    -p, --push
        push the apk to dicrect path.
    '''
    pass

#######################################################
def pushAPK(path):
    '''
    Push the apk to devices
    '''
    try:
        if getRootRemount() and os.path.exists(path.getOutFromPath()):
            try:
                if runCommand(False, "adb push " + path.getOutFromPath() + " " + path.getOutToPath()):
                #if runCommand(False, "adb push " + path.getOutFromPath() + " " + path.getOutToPath(), "adb reboot"):
                    pass
                    #print "push ok."
            except Exception,e:
                print e
    except Exception,e:
        print "========push error!========\n"
        print e
        sys.exit(1)
#######################################################
def pullAPK():
    pass

#######################################################
def getNewestAPK(fileName):
    fileDir = CONFIG_FILE.get("tmpDir")
    if os.path.exists(fileDir):
        fileList = []
        for f in os.listdir(fileDir):
            if fileName in f:
                fileList.append(f)
                print f
        if fileList.count > 0:
            print "waitting for ...."
    else:
        return "Error"

#######################################################
def restore(fileName):
    if fileName in CONFIG_FILE:
        lastedAPK = getNewestAPK(fileName)
        #pushAPK()
    pass

#######################################################
def obtainPackage(finaPath):
    return ""

#######################################################
def getPid(packageName):
    cmd = "adb shell ps |grep -iE \"" + packageName + "$\" | sed \'/ \+/s// /g\' | cut -f 2 -d \' \'"
    pid = runCommand(True, cmd)[1]
    return pid

#######################################################
def killApk(path):
    package = path.outpackage

    pid = getPid(package)
    if pid > 0:
        cmd = "adb shell kill " + str(pid)
        runCommand(True, cmd)
    else:
        print "kill fail."

#######################################################

if __name__ == '__main__':
    opts, args = getopt.getopt(sys.argv[1:], "hki:s:ptr:") #后面带有：号表示该选项后面需要带上参数
    p = path.Path(os.getcwd())
    for op, value in opts:
        #print "%s ---> %s" % (op, value)
        if op == "-i":
            pass
        if op == "-r":
            restore(value)
        if op == "-s": #store
            store(value)
        if op == "-h":
            print usage.__doc__
        if op == "-p":
            pushAPK(p)
        if op == "-k":
            killApk(p)
            pass
        if op == "-t":
#            print getNewestAPK("cherrytree")
            #f = write_config("/home/alex/Desktop/scripts/adbInstall/config.ini","c", "F")
            conf = config.Config("/home/alex/Desktop/scripts/adbInstall/config.ini")
            print conf.read_config("/home/alex/Desktop/scripts/adbInstall/config.ini","c") 
    sys.exit()