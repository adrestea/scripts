#!/usr/bin/python3
# -*- coding: utf-8 -*-
from urllib3 import request

from bs4 import BeautifulSoup
import json
import requests
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class WordsInfo:
    _url_base_search = 'https://www.shanbay.com/api/v1/bdc/search'
    _url_details_search = 'https://www.shanbay.com/bdc/vocabulary/{}/'
    _response = None

    def __init__(self, word):
        # self._word = word
        # self._response = self.get_response(self._url_base_search, {'version': 2, 'word': self._word})
        # self._url = self._response.url
        # self._response_str = self._response.text
        # self._id = self.get_id()

        self._id = 1285
        self._details_response = self.get_response(self._url_details_search.format(str(self._id)))
        # print(self._details_response.content)
        self.parase_html(self._details_response.content)
        # self.parase_html('/home/archermind/Desktop/ttttt/test.html')

    def parase_html(self, html):
        page = BeautifulSoup(html, "html.parser")
        print BeautifulSoup(str(page.find_all('h1', class_="content pull-left")), "html.parser").text.encode("utf-8")




        # learning_word = BeautifulSoup(str(page.find_all('div', id='learning_word', class_='row')), "html.parser")
        # self._word = learning_word.find('h1', class_="content pull-left")
        # self._explain = (learning_word.find('div', class_="cndf span7"))
        # print self._word.encode("utf-8").encode('utf-8')
        # print self._explain.text.encode('utf-8')

        # learning_examples_box = BeautifulSoup(str(page.find_all('div', id='learning-examples-box', class_='row')),
        #                                       "html.parser")
        # notes_box = BeautifulSoup(str(page.find_all('div', id='notes-box', class_='row')), "html.parser")


    def get_content(self):
        return self._details_response.text

    def get_id(self):
        try:
            return json.loads(self._response_str)['data']['id']
        except KeyError as err:
            print "error ---> KeyError"

    def get_response(self, url, params=None):
        """
        :param url:base_url = 'http://httpbin.org/'
        :param params:the dic of params, format like this:
        params = {
            'name': 'yitian',
            'age': 22,
            'friends': ['zhang3', 'li4']
        }
        :return:
        # 结果: http://httpbin.org/get?name=yitian&age=22&friends=zhang3&friends=li4

        response属性名	结果
        text	HTTP字符
        encoding	响应编码，这个值可以改变，改变之后text属性也会根据编码而变化
        content	未编码的二进制数据
        json()	返回JSON数据
        raw	结果的原始字节流
        url	请求的URL
        status_code	状态码
        headers	请求头字典
        cookies	cookies字典
        history	如果发生重定向，所有请求对象都会保存到这里
        """
        return requests.get(url, params=params)


if __name__ == '__main__':

    # import simplejson as json

    # res = get_response_with_params(url_base_search, params)
    # data = json.loads(get_text_by_decode(res))
    # print b'\u02d0'.decode('utf-8')
    print 'bɔːs'

    # info = WordsInfo('boss')
    # / bɔːs /
    # / b\u0254\u02d0s /
    # print info.get_content()
    print b'\xe4\xb8\xad'.decode('utf-8')
