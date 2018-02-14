#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from utils.httpUtils import *
from utils.fileUtils import *
from bs4 import BeautifulSoup
import re

url = "http://webosss.com/tool/socket"
fileName = "tests"

def get(match1, match2, result):
    lis = []
    res = re.compile(match1).findall(result)
    pattern = re.compile(match2)
    lis = []
    for r in res:
        lis.append(pattern.findall(r))
    return lis

def spli(match1, match2, result, index):
    lis = []
    res = re.compile(match1).findall(result)
    pattern = re.compile(match2)
    lis = []
    for r in res:
        lis.append(pattern.split(r)[index].replace("<", ""))
    return lis

def getPort(html):
    return get(r'Port：\d+', r'\d+', result)

def getMethod(html):
    return spli(r'Method:\S+<', r':', html, 1)

def getIpAddress(html):
    return get(r'IP Address.*</span>\s\s', r'\w+\.\w+\.\w+', result)


def getPassword(html):
    return get(r'Password.*</span>\s\s', r'\d+', result)

if __name__ == '__main__': 

    if not isExist(fileName):
        writeFile(fileName, obtainHTML(url))
    
    result = readFileAll(fileName)
    soup = BeautifulSoup(result, "lxml")
    #print soup.find_all(class_='hover-text')
    #hoverText = soup.find_all("div", class_='hover-text')
    
    #print hoverText
    #print getIpAddress(result)
    #print getPort(result)
    #print getMethod(result)
    print getPassword(result)

    shadowsockList = {}
    #for t, m, a, p in getPort(result), getMethod(result), getIpAddress(result), getPassword(result):
    print len(getIpAddress(result))
    for index in range(len(getIpAddress(result))):
        print getPort(result)[index], getMethod(result)[index], getIpAddress(result)[index], getPassword(result)[index]

