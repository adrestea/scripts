#!/usr/bin/python3
# -*- coding: utf-8 -*-
# filename: HelloWorld.py

from urllib.parse import urlparse
from urllib import request
from bs4 import BeautifulSoup
import sys


class HtmlHandler:
    __request_url = ""
    __page_next_url = ""
    __soup = None
    __title = ""

    def getNextUrl(self):
        pb_next = self.__soup.find(id='pb_next')
        return self.getBaseUrl() + pb_next.attrs["href"]

    def download_html_content(self):
        head = {}
        head[
            'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, ' \
                            'like Gecko) Chrome/18.0.1025.166  Safari/535.19 '
        page = request.urlopen(self.__request_url)
        soup_text = page.read().decode('utf-8', 'ignore')
        return soup_text.replace('\xa0', '')

    def __init__(self):
        pass

    def download_content(self, request_url):
        self.__request_url = request_url
        content = self.download_html_content()
        self.__soup = BeautifulSoup(content, "html.parser")
        self.__title = self.__soup.title

    def save_content(self):
        try:
            f = open("content.txt", "a+")
            chapter_content = self.__soup.find(id='chaptercontent', class_="Readarea ReadAjax_content")
            if chapter_content:
                c = chapter_content.text.replace("    ", "\n    ")
                c = '\n\n' + "--" * 40 + '\n' + self.__title.text + '\n' + c
                f.write(c)
        finally:
            f.close()

    def parseHtmlContent(self):
        pass

    def getBaseUrl(self):
        print("--" * 40, "getBaseUrl")
        o = urlparse(self.__request_url)
        return o.scheme + "://" + o.netloc

    def getContents(self):
        pass

    def getTitle(self):
        return self.__title


def download_yanjueshancun():
    url = 'http://wap.xxbiquge.com/2_2226/3215553.html'
    htmlHandler = HtmlHandler()
    try:
        while url != "":
            htmlHandler.download_content(url)
            htmlHandler.save_content()
            url = htmlHandler.getNextUrl()
            print(url)
    except AttributeError:
        print("Oops!")

    print("ok!")


if __name__ == "__main__":
    download_yanjueshancun()
