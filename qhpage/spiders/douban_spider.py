# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from scrapy import Spider, Request
from scrapy.selector import Selector
#from scrapy.utils.response import get_base_url
#from scrapy.spiders import CrawlSpider, Rule
#from scrapy.linkextractors import LinkExtractor
from qhpage.items import DoubanBookItem

class DoubanBookSpider(Spider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://book.douban.com",
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@class="section ebook-area"]//ul[@class="list-col list-col5"]/li//div[@class="title"]')
        for site in sites:
            title = site.xpath('a/@title').extract()
            link = site.xpath('a/@href').extract()
            title, link = title[0], link[0]
            yield Request(url=link, callback=self.parse_info)

    def parse_info(self, response):
        soup = BeautifulSoup(response.body)
        bookInfo = soup.findAll('div', attrs={'class':'article-profile-bd'})
        if bookInfo:
            bookInfo = bookInfo[0]
            item = DoubanBookItem()
            item['title'] = "".join(bookInfo.findAll('h1', attrs={'class':'article-title'})[0].strings)
            item['author'] = "".join(bookInfo.findAll('p', attrs={'class':'author'})[0].strings)
            item['category'] = "".join(bookInfo.findAll('p', attrs={'class':'category'})[0].strings)
            item['price'] = bookInfo.findAll('div', attrs={'class':'action-buttons btns-large'})[0]['data-readable-price']
            return item
