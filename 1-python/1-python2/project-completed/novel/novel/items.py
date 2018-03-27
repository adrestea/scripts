# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    novel_url = scrapy.Field()
    serial_status = scrapy.Field()
    serial_number = scrapy.Field()
    category = scrapy.Field()
    name_id = scrapy.Field()
    content = scrapy.Field()


class TtxlContentItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    desc = scrapy.Field()
