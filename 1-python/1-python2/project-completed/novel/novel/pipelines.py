# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 对于乱序的处理思路:使用url标志唯一区别然后合并为一个文件
# ls *.html | sort -n |xargs -I {} cat {}  >> ttxl
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


class NovPipeline(object):
    def process_item(self, item, spider):
        print("--------------------------" + item['title'])
        # with open(settings.FILE_NAME, 'a+') as f:
        file = "chapters/" + item['desc'].split("/")[-1]
        # file = item['title'].split(" ")[0] + ".txt"
        with open(file, 'a+') as f:
            f.write(item['title'])
            f.write(item['content'])
            f.write('\n\n')
        return item
