#!/usr/bin/env python
#coding:utf-8
import os
import re
import json
# ffprobe 需放置在 system32, not user's PATH
#获取视频信息=================
def getVideoInformation(js):
    iVideoWidth = 0
    iVideoHeight = 0
    iVideoBitRate = 0
    iVodeoDuration = 0
    iAllBitRate = 0
    strCodecName = 0

    arrStreams = js['streams']

    for stream in arrStreams:
        if(stream["codec_type"] == u'video'):
            strCodecName = stream['codec_name']
            iVideoWidth = int(stream['width'])
            iVideoHeight = int(stream['height'])
            iVodeoDuration = int (stream['duration_ts'])
            # h264 可能没有这一项
            if 'bit_rate' in stream.keys():
                iVideoBitRate = int(stream['bit_rate'])
                break
    iAllBitRate = int(js['format']['bit_rate'])
    return 'CodecName (%s), width(%d), height(%d), video bit_rate(%d), all bit_rate (%d), duration (%d)' % (strCodecName, iVideoWidth, iVideoHeight, iVideoBitRate, iAllBitRate, iVodeoDuration)

#获取文件夹里的所有文件名称=============
g_fileList = []
def getFiles(path):
    if os.path.exists(path):
        files = os.listdir(path)
        for f in files:
            subpath=os.path.join(path,f)
            if os.path.isfile(subpath):
                g_fileList.append(subpath)
            else:
                getFiles(subpath)

# ffprobe 需放置在 system32, not user's PATH
# 调用ffprobo 获取信息的json格式
def getJsonString(strFileName):
    strCmd =  'ffprobe -v quiet -print_format json -show_format -show_streams -i "' +  strFileName  + '"'
    mystring = os.popen(strCmd).read()
    return  mystring

#过滤视频文件=================
# 按扩展名过滤          
def filterExname (fileList, arrExtnames):
    filterList = []
    for strFile in fileList:
        strLowFileName = strFile.lower() # 转小写先  

        for strExtName in arrExtnames :
            if strLowFileName.endswith(strExtName):
                filterList.append(strFile)
    return filterList


arrExtName = ['.mkv', '.rmvb', '.rm', '.wmv', '.avi', '.mp4', '.mov', '.mpg', '.xvid', '.asf', '.mpeg', '.vob', '.3gp', '.flv', '.ts']  

if __name__ == "__main__":
    getFiles(os.getcwd())
    arrVideoFiles = filterExname(g_fileList, arrExtName)
    # UnicodeDecodeError: 'utf8' codec can't decode byte 0xc0 in position 57: invalid start byte
    for strFileName in arrVideoFiles:
        filecontent = getJsonString(strFileName)
#        print "filecontent=%s\n" % filecontent
        try:
            js = json.loads(filecontent)
            info = getVideoInformation(js)
            print 20 * "*"
            print strFileName
            print info
        except Exception, e:
            print Exception,":",e, strFileName
    print 20 * "*"
    exit(0)
