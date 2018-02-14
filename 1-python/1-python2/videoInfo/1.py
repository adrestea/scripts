#!/usr/bin/env python
#coding:utf-8
import os
import re
import json
# ffprobe 需放置在 system32, not user's PATH

#获取视频信息=================
def getVideoInformation(arrStreams, js):
    iVideoWidth = 0
    iVideoHeight = 0
    iVideoBitRate = 0
    iAllBitRate = 0
    strCodecName = ''

    for stream in arrStreams:
        if(stream['codec_type'] == 'video'):
            strCodecName = stream['codec_name']
            iVideoWidth = int(stream['width'])
            iVideoHeight = int(stream['height'])
            # h264 可能没有这一项
            if 'bit_rate'  in stream.keys():
                iVideoBitRate = int (stream['bit_rate'])
                break

    iAllBitRate = int(js['format']['bit_rate'])
    print  'CodecName (%s), width(%d), height(%d), video bit_rate(%d), all bit_rate (%d)' % (strCodecName, iVideoWidth, iVideoHeight, iVideoBitRate, iAllBitRate )

#获取文件夹里的所有文件名称=============
def getFilesWithPath():
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

# 如果是网络路径，可以先映射到本地, python有可能不支持网络路径 \\  
#getFiles('.')  

    print 'g_fileList len = ', len(g_fileList)
    arrExtName = ['.mkv', '.rmvb', '.rm', '.wmv', '.avi', '.mp4', '.mov', '.mpg', '.xvid', '.asf', '.mpeg', '.vob', '.3gp', '.flv', '.ts']  
    arrVideoFiles = filterExname (g_fileList, arrExtName)

# 过滤大的码率文件====
# 设置单位像素 比特率 阈值 2.5 - 4.0  
PIEXL_RATE_MAX = 3.9
def isLargeBps(iWidth, iHeight, iBitrate):  
    # 基准 每像素字节数  
    fCurrentBitRatePixel = float(iBitrate) / (iWidth * iHeight)  
    print  'isNeedConvert input = ', iWidth, iHeight, iBitrate, fCurrentBitRatePixel  
    return (fCurrentBitRatePixel > PIEXL_RATE_MAX)  