#!/usr/bin/python
#coding=utf-8
import os
import commands
import sys


list_dir = {"JrdTimeTool":['./alto45/custpack/app/unremoveable/JrdFileManager_v1.6.002.0.apk']}

def run_adb(cmd, flag, string_flag, enable_succ, string_succ, enable_fail, string_fail):
    status, output = commands.getstatusoutput(cmd)
    if status == flag and string_flag in output:
        if enable_succ:
            print string_succ
    else:
        if enable_fail:
            print string_fail

def main():
    print sys.argv
    run_adb("adb devices", 0, "\tdevice", 1, "device connection successed!", 1, "device connection failed!");
    run_adb("adb root", 0, "adbd is already running as root", 1, "root successed", 1, "root failed");
    run_adb("adb remount", 0, "remount succeeded", 1, "remount succeeded!", 1, "remount faied!");
    run_adb('adb shell mount -o remount /custpack', 0, "", 1, "remount custpack succeeded!", 1, "remount custpack faied!");

    if list_dir.has_key(sys.argv[1]):
        print list_dir.get(sys.argv[1])
#        run_adb("adb push ", 0, "remount succeeded", 1, "", 1, "");

if __name__ == '__main__':
    main()












#status, output = commands.getstatusoutput("adb root")
#if status != 0 or "adbd is already running as root" not in output:
#    print output
#    return

 
#status, output = commands.getstatusoutput("adb remount")
#if status == 0 and "adbd is already running as root" in output:
#else:
#    print output
#    return
#
#if status == 0:
#    print "device connection successed!"
#else:
#    return

