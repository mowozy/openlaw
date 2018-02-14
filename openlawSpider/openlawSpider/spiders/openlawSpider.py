#coding:utf-8

import scrapy

from ..items import OpenlawspiderItem

from scrapy.crawler import CrawlerProcess

class openlawSpider(scrapy.Spider):
    name = 'openlaw'
    allowed_domain = []
    start_urls = ["http://openlaw.cn/search/judgement/type?causeId=4d4ed2b0aea446f5bd5e1432e33c27e5&selected=true"]

    def parse(self, response):
        papers = response.xpath(".//*[@class='ht_kb type-ht_kb status-publish format-standard hentry']")
        for paper in papers:
            url = paper.xpath(".//*[@class='entry-title'/a/@href]").extract()[0]
            title = paper.xpath(".//*[@class='entry-title'/a/text()")
            item = OpenlawspiderItem(url=url, title=title)
            yield item
        new_url = response.xpath('//a[@class="next page-numbers"//@href]')
        if new_url:
            yield scrapy.Request(new_url, callback=self.parse)