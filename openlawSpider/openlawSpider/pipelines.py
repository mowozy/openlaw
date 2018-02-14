# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib
import json

from scrapy.exceptions import DropItem
from ..openlawSpider import settings

class OpenlawspiderPipeline(object):

    def __init__(self):
        self.file = open('papers.json', 'wb')

    def process_item(self, item, spider):
        if item['title']:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
        else:
            raise DropItem("missing item" % item)