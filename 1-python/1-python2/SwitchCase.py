#!/usr/bin/python
#coding=utf-8
#import os, sys, getopt
#import threading
#import glob
#import os
#import fnmatch

'''
python中swith...case的实现
'''
if __name__ == '__main__':
    context = {1: 'default', 2:'21'}
#    for i, j in enumerate(context):
#        print i, j
    choosed = input('input:')
#    print type(choosed)
    assert isinstance(choosed, int)
    print context.get(choosed)