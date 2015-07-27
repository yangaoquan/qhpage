import re
import json

from scrapy import Spider
from scrapy.selector import Selector
from scrapy.spiders import spiders
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from qhpage.items import DoubanSubjectItem


class DoubanBookSpider(CrawlSpider):
    name = "dbspider"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://book.douban.com/tag/"
    ]
    #rules = [
    #    Rule(LinkExtractor(allow=('//div[@class="article"]/div[@class=""]/div')), callback='parse_2'),
    #    Rule(LinkExtractor(allow=("/tag/[^/]+/?$", )), follow=True),
    #    Rule(LinkExtractor(allow=("/tag/$", )), follow=True),
    #]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="article"]/div[@class=""]/div')

        for item in questions:
            titles = item.xpath('./table/tbody/tr/td/a/text()').extract()
            links = item.xpath('./table/tbody/tr/td/a/@href').extract()
            cate = item.xpath('./a/@name').extract()[0]
            for title, link in zip(titles, links):
                item = DoubanSubjectItem()
                item['title'] = title
                item['link'] = link
                item['content_intro'] = cate
                yield item


    def parse_2(self, response):
        items = []
        sel = Selector(response)
        print "xxxx", sel
        sites = sel.css('#tag-title-wrapper')
        for site in sites:
            #item = DoubanSubjectItem()
            #item['title'] = site.css('h1 span::text').extract()
            #item['link'] = response.url
            #item['content_intro'] = site.css('#link-report .intro p::text').extract()
            #items.append(item)
            # print repr(item).decode("unicode-escape") + '\n'
            print "------->", site
        # info('parsed ' + str(response))
        return items

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        info('parsed ' + str(response))

    def _process_request(self, request):
        info('process ' + str(request))
        return request
