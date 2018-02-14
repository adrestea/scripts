#!/usr/bin/env python
#-*- coding: utf8 -*-

import xlrd
import sys
from pyExcelerator import *
 
reload(sys)
print sys.getdefaultencoding()
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding()

a = {"a": u"çö"}
b = "çö"
assert b == a['a']
assert b.decode('utf-8') == a['a'].decode('utf-8')

#w = Workbook()
#ws = w.add_sheet(u'Sheet1')

fname = "/home/user/Downloads/xlsResult_0405.xls"
bk = xlrd.open_workbook(fname)
shxrange = range(bk.nsheets)
try:
    sh = bk.sheet_by_name(u"TS_ロック")
except:
    print "no sheet in %s named Sheet1" % fname

rows = sh.row_values(3) # 获取第四行内容
cols = sh.col_values(5) # 获取列内容
for r in cols:
    print "value:%s" % (r)
print " * " * 20
ncols = sh.ncols
nrows = sh.nrows
print "nrows %d, ncols %d" % (nrows, ncols)
print " * " * 20