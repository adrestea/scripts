#!/usr/bin/python
#coding=utf-8


'''
python中文件路径的处理
'''

'''
1 获取某指定目录下的所有子目录的列表
'''
import os
def getDirList(p):
    p = str(p)
    if p == "":
        return []
#    p = p.replace("/","\\")
#    if p[ -1] != "\\":
#         p = p+"\\"
    a = os.listdir(p)
    b = [x for x in a if os.path.isdir(p + os.path.sep + x)]
    return b


if __name__ == '__main__':
    print getDirList('/home/alex/Desktop/test')

'''
删除文件夹,未验证！
'''
def RemoveFolderOs(sourceDir):
    for root, dirs, files in os.walk(sourceDir):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

'''
import os

s = os.getcwd()	#取得当前目录

import time
folderName = time.strftime(r"%Y-%m-%d_%H-%M-%S",time.localtime())	#根据当前时间生成文件名
os.makedirs(r'%s/%s'%(os.getcwd(),folderName))	#创建目录

os.chdir( "C:\\123")	#更改当前目录，当指定的目录不存在时，引发异常。

fpath , fname = os.path.split( "c:\\123\\456\\test.txt" )	#将一个路径名分解为目录名和文件名两部分
fpathandname , fext = os.path.splitext( "c:\\123\\456\\test.txt" )	#分解文件名的扩展名

b = os.path.exists( "你要判断的路径")	#判断一个路径（目录或文件）是否存在
b = os.path.isfile( "你要判断的路径")	#判断一个路径是否文件
b = os.path.isdir( "你要判断的路径")	#判断一个路径是否目录
L = os.listdir( "你要判断的路径")	#获取某目录中的文件及子目录的列表

os.rmdir( path )   #删除的子目录
os.remove(filename)   # filename: "要删除的文件名"
os.name( oldfileName, newFilename)	#文件改名
os.removedirs（r“c：\python”） #删除多个目录
os.path.isabs() #判断是否是绝对路径

os.path.splitext() #分离扩展名
os.path.dirname()   #获取路径名
os.path.basename()  #获取文件名
os.system() #运行shell命令
os.getenv() 与os.putenv()    #读取和设置环境变量
os.linesep    #给出当前平台使用的行终止符,Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.name #指示你正在使用的平台       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
os.mkdir（“test”）    #创建单个目录
os.stat（file）   #获取文件属性
os.chmod（file）  #修改文件权限与时间戳
os.exit（）   #终止当前进程
os.path.getsize（filename）   #获取文件大小

复制文件：
shutil.copyfile("oldfile","newfile")       oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")            oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
复制文件夹：
shutil.copytree("olddir","newdir")        olddir和newdir都只能是目录，且newdir必须不存在
shutil.rmtree("dir")    空目录、有内容的目录都可以删



example:



# -*- coding:utf-8 -*-
import re
import os
import time
#str.split(string)分割字符串
#'连接符'.join(list) 将列表组成字符串
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            i+=1 #注意这里的i是一个陷阱
        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用


img_dir = 'D:\\xx\\xx\\images'
img_dir = img_dir.replace('\\','/')
start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))
'''