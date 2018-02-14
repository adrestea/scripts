#!/usr/bin/python
#coding=utf-8
import os
import sys
import commands

def updates(path):
    while True:
        print "---------------->  updating %s  <-------------" % (path)
        status, output = commands.getstatusoutput('svn update ' + path)
        if status == 0:
            print output
            break
        else:
            print "unlicking the directory..."
            tatus, output = commands.getstatusoutput('svn cleanup ' + path)
            if status == 0:
                print "unlock successed!"
            else:
                print "unlock failed"
                return
    
def main():
    UPDATE_BASEDIR = '~/RapidSVN/'
    OUTPUTDIR = 'Tcl-project/output/'
    PROJECTDIR = '项目管理'

    updates(os.path.join( UPDATE_BASEDIR, OUTPUTDIR))
#    update(os.path.join( UPDATE_BASEDIR, PROJECTDIR))
    
if __name__ == '__main__':
  main()
