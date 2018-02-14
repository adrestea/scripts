#!/usr/bin/python
import urllib.request,io,os,sys
req = urllib.request.Request("http://bugzilla.tcl-ta.com/show_bug.cgi?id=852922")
f = urllib.request.urlopen(req)
s = f.read()
s = s.decode('gbk','ignore')
mdir = sys.path[0]+'/'
file = open(mdir+'admin4.txt','a',1,'gbk')
file.write(s)
file.close()