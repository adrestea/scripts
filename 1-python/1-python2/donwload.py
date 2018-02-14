#coding=utf-8
import threading
from time import ctime,sleep
import subprocess

def music(func):
    for i in range(2):
        print("I was listening to %s(%s). %s"%(func, i, ctime()))
        sleep(1)

def move(func):
    for i in range(3):
        print("I was at the %s(%s)! %s" %(func, i, ctime()))
        sleep(5)

def downloadCodes():
	command=["ls","-l"]
#	command="repo sync -c --no-tags"
	pp=subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	sleep(10)
	return pp

def startDownloadDamon():
#    dtown = threading.Thread(target=music, args=(u'爱情买卖',))
    dtown = threading.Thread(target=downloadCodes)
    dtown.setDaemon(True)
    dtown.start()
	print("pid=%s"%(dtown.ident()))
#	print("pid=%s" %("5"))
#	while 1:
#		if dtown.isAlive():
#			sleep(10)
#		else:
#			sleep(5)
    dtown.join()

if __name__ == '__main__':
    deamon = threading.Thread(target=startDownloadDamon)
    print("Begin at at %s"%(ctime()))
    deamon.setDaemon(True)
    deamon.start()
    deamon.join()
    print("All over at %s" %ctime())
