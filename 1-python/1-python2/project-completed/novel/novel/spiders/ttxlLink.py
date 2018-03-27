#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.selector import Selector
from nov.items import TtxlContentItem

reload(sys)
sys.setdefaultencoding('utf-8')


class TtxlSpider(scrapy.Spider):
    name = 'ttxl'
    allow_domains = ['biqubook.com']
    base_url = 'http://www.biqubook.com'
    start_urls = ['http://www.biqubook.com/3_3097/']

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//body/div[@class="listmain"]/dl/dd')
        index = 0
        for site in sites:
            url = self.base_url + site.xpath('a/@href').extract()[0]
            yield Request(url, callback=self.parse_content, priority=index)

    def parse_content(self, response):
        item = TtxlContentItem()
        soup = BeautifulSoup(response.body, 'lxml')
        item['title'] = soup.find('h1').string
        item['content'] = soup.find(id='content', class_='showtxt').text
        item['desc'] = response.request.url

        return item
