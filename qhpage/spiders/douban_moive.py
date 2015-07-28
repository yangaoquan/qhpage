import re
import json

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.spiders import spiders
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from qhpage.items import DoubanMoiveItem

class MoiveSpider(CrawlSpider):
    name="doubanmoive"
    allowed_domains=["movie.douban.com"]
    start_urls=["http://movie.douban.com/top250"]
    rules=[
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/top250\?start=\d+.*'))),
        Rule(LinkExtractor(allow=(r'http://movie.douban.com/subject/\d+')),callback="parse_item"),
    ]
     
    def parse_item(self, response):
        sel = Selector(response)
        item = DoubanMoiveItem()
        item['url'] = response.url
        item['name'] = sel.xpath('//*[@id="content"]/h1/span[1]/text()').extract()
        item['year'] = sel.xpath('//*[@id="content"]/h1/span[2]/text()').re(r'\((\d+)\)')
        item['score'] = sel.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()').extract()
        item['vote'] = sel.xpath('//*[@id="interest_sectl"]/div/p[2]/a/span/text()').re(r'\d+')
        return item

