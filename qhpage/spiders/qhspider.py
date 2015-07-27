# -*- coding:utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector

from qhpage.items import QhpageItem
 
class QhpageSpider(Spider):
    name = "qhpage"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        "http://stackoverflow.com/questions?pagesize=50&sort=newest",
    ]
    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]')

        for question in questions:
            item = QhpageItem()
            item['name'] = question.xpath('./h3/a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath('./h3/a[@class="question-hyperlink"]/@href').extract()[0]
            item['title'] = question.xpath('./div[@class="excerpt"]/text()').extract()[0]
            yield item
