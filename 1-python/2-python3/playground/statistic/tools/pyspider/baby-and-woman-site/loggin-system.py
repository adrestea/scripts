#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re
import traceback
import urllib
import urllib.request
import http.cookiejar
from collections import deque

print("\n\n*************** Step 1: visit index page and get the token generated in server side ******************")
url = "http://gitlab.your_company_addr.com/users/sign_in"
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Host': 'www.zhihu.com',
    'DNT': '1'
    # 'Cookie': '_gitlab_session=f00c50db7dc2c83989419079760e5786'
}

def test():
    import  os
    os.getcwd()

def loggin(token):
    print("\n\n*************** Step 2: login the server with username, password and token generated before **********")
    url = "http://gitlab.your_company_addr.com/users/auth/ldapmain/callback"
    postDict = {
        'utf8': '✓',
        'username': 'zhuoyp001',
        'password': '********',
        'authenticity_token': token
    }

    postData = urllib.parse.urlencode(postDict)
    postData = postData.encode('utf-8')
    res = opener.open(url, postData)
    print(res.status, res.reason)
    if (res.status != 200):
        print("login failed")
        exit()

    print('login successfully!')


def scraping():
    print("\n\n*************** Step 3: begin scraping... **********")
    baseUrl = "http://gitlab.your_company_addr.com/explore/projects"
    project_queue = deque()
    visited = set()
    current_page = 1
    page_amount = 3
    url = baseUrl
    while current_page <= page_amount:
        url = baseUrl + "?page=" + str(current_page)
        print("正在抓取第 " + str(current_page) + " 页, " + url)
        try:
            urllop = opener.open(url, timeout=1000)
            data = urllop.read().decode("utf-8")
        except:
            print("error")
            continue
        linkre = re.compile('<a class="project" .*href="(/.+?)"')  # match projects
        for x in linkre.findall(data):
            project_queue.append(x)
            print("加入待爬页面：" + x)
        current_page += 1
        url = baseUrl + "?page=" + str(current_page)
    return project_queue


def access_echo(project_queue):
    print("\n\n*************** Step 4: visit each project and aggregate data")

    class Issue:
        def __init__(self, project=None, open=0, closed=0):
            self.project = project
            self.open = open
            self.closed = closed

    projects_found = 0
    project_list = []
    while project_queue:
        project = project_queue.popleft()
        project_url = "http://gitlab.your_company_addr.com" + project + "/issues"
        try:
            project = str(project).rsplit(sep="/", maxsplit=1)[-1]
            issue = Issue(project)
            project_page = opener.open(project_url, timeout=1000)
            data = project_page.read().decode("utf-8")

            openre = re.compile('<span>Open</span>.*<span class="badge">(.+?)</span>')
            for openNum in openre.findall(data):
                projects_found += 1
                issue.open = int(openNum)
                # 省略对其他字段的提取
            project_list.append(issue)
        except:
            print("error page: " + project_url)
            traceback.print_exc()
            continue


def analyze(project_list):
    print("\n\n*************** Step 5: analyze data and write pic")
    project_names = []
    project_open = []
    project_closed = []
    N = 0
    for i in range(len(project_list)):
        if project_list[i].all > 0:
            project_names.append(project_list[i].project)
            project_open.append(project_list[i].open)
            project_closed.append(project_list[i].closed)
            N += 1

    names = tuple(project_names)
    open = tuple(project_open)
    closed = tuple(project_closed)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.65  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, open, width, color='#d62728')
    p2 = plt.bar(ind, closed, width, bottom=open)

    plt.ylabel('issues')
    plt.title('project issues')
    plt.xticks(ind, names)
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('open issues', 'closed issues'))

    plt.show()


def getToken(data):
    cer = re.compile('name=\"authenticity_token\" value=\"(.+?)\"')
    strlist = cer.findall(data)
    return strlist[0]


def getOpener(head):
    # deal with the Cookies
    cj = cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


opener = getOpener(header)
op = opener.open(url)
data = op.read().decode("utf-8")
token = getToken(data)
print(token)
loggin(token)
