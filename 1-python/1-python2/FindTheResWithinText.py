#!/usr/bin/python
#coding=utf-8
import os
import optparse
'''
文件查找
'''


'''
1:精确查找
调用为：
    #print "Found File at %s" % file
    #options, args = parse_args()
    #find_file = list(search_file("find /home/alex/Desktop/test/ -type f |grep -i ab", "/home/alex/Desktop/res"))
'''
def search_file(filename, search_path=os.environ['PATH'], pathsep=os.pathsep):#os.pathsep是分隔符';'
    for path in search_path.split(os.pathsep):
        candidate = os.path.join(path, filename)#预选路径
        if os.path.isfile(candidate):
            yield os.path.abspath(candidate) #用生成器可以方便控制返回的数据.可以使用.next()等方法只返回下一个子项

'''
参数解析
'''
def parse_args():#帮助提示
    usage = u'''这是一个查找文件夹路径中是否有文件指定文件的脚本,
第一个参数是要找的文件名，第二个是路径'''
    parser = optparse.OptionParser(usage)
    help = u'要查找的文件名字'
    parser.add_option('--filename', help=help)#type='int',
    help = u'查找的路径多个路径以;分隔'
    parser.add_option('--path', help=help, default='e:')
    options, args = parser.parse_args()
    return options, args

'''
通过运行Bash命令find和grep联合来模糊查找res文本里面包含的文字相对应的资源情况
'''
def search_file_by_bash():
    res_File = "/home/alex/Desktop/res"
    cmd = "find /home/alex/Desktop/test/ -type f |grep -i "
    f = open(res_File, "r")
    for line in f:
        line_num = os.popen(cmd + line.strip('\n')).read()
        print(line.strip('\n')+"\t\t\t\t----------------->")
        print(line_num+"\n")

'''
使用subprocess.Popen来运行bash命令
限制是在使用的时候不能够通过管道传递
'''
def search_file_by_bash_():
    import subprocess
    #subprocess.Popen(cmd, shell=True)
    #print handle.communicate()[0]

if __name__ == '__main__':
    search_file_by_bash()