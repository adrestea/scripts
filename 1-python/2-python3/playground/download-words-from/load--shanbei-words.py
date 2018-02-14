#!/usr/bin/python
# -*- coding: utf-8 -*-

from http import cookiejar
import urllib2
import urllib
import requests


def get_direct_by_url(url):
    response = urllib2.urlopen(url)
    html = response.read()
    print html


def gett(url):
    request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.206738964.1516669890; csrftoken=T63JsVx6K7uKMThDywZi9DnRulhm7U77; sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrJSsxLz9dLzs8rKcpM0gMp0YPKFuv55qek5jhB1eogG5AJ1GtoYGBgYWRkal4LADKHIIE:1edn8L:hy9YF0Hiy_1E7zEdX24Cfnzlytc"; userid=100082257; __utmc=183787513; __utmz=183787513.1516669945.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); language_code=zh-CN; __utma=183787513.206738964.1516669890.1517452758.1517461874.10; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vYmlsZV9hMWExMGIyZjMwIiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMDAwODIyNTcsImV4cCI6MTUxODMyNzA2N30.LF0OZH1Z6Yf3Piz27Ly9NDEiODdYXimWZoCI6uoM7t0; __utmt=1; __utmb=183787513.57.10.1517461874',
        'Host': 'www.shanbay.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url, headers=request_headers)
    html = response.text
    print(html)


def get_content_by_cookie(url):
    request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.206738964.1516669890; csrftoken=T63JsVx6K7uKMThDywZi9DnRulhm7U77; sessionid=".eJyrVopPLC3JiC8tTi2KT0pMzk7NS1GyUkrJSsxLz9dLzs8rKcpM0gMp0YPKFuv55qek5jhB1eogG5AJ1GtoYGBgYWRkal4LADKHIIE:1edn8L:hy9YF0Hiy_1E7zEdX24Cfnzlytc"; userid=100082257; __utmc=183787513; __utmz=183787513.1516669945.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); language_code=zh-CN; __utma=183787513.206738964.1516669890.1517452758.1517461874.10; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1vYmlsZV9hMWExMGIyZjMwIiwiZGV2aWNlIjowLCJpc19zdGFmZiI6ZmFsc2UsImlkIjoxMDAwODIyNTcsImV4cCI6MTUxODMyNzA2N30.LF0OZH1Z6Yf3Piz27Ly9NDEiODdYXimWZoCI6uoM7t0; __utmt=1; __utmb=183787513.57.10.1517461874',
        'Host': 'www.shanbay.com',
        'Pragma': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    data = urllib.urlencode(request_headers)  # 编码工作
    req = urllib2.Request(url, data)  # 发送请求同时传data表单
    response = urllib2.urlopen(req)  # 接受反馈的信息
    the_page = response.read()  # 读取反馈的内容
    print the_page


if __name__ == '__main__':
    url = 'https://www.shanbay.com/bdc/vocabulary/1285'
    # get_direct_by_url(url)
    # get_content_by_cookie(url)
    gett(url)

    '''
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    # response = opener.open('http://www.baidu.com')
    response = opener.open('https: // www.shanbay.com / api / v1 / bdc / search /?version = 2 & word = boss')
    # 打印cookie信息
    for item in cookie:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)
'''
