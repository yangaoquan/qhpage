# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class QhpageItem(Item):
    # define the fields for your item here like:
    name = Field()
    url = Field()
    title = Field()

class DoubanbookItem(Item):
    name = Field()
    title = Field()
    link = Field()
    desc = Field()
    num = Field()

class DoubanSubjectItem(Item):
    title = Field()
    link = Field()
    info = Field()
    rate = Field()
    votes = Field()
    content_intro = Field()
    author_intro = Field()
    tags = Field()

class DoubanBookItem(Item):
    title = Field()
    author = Field()
    publisher = Field()
    category = Field()
    price = Field()


from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join

class DmozItem(Item):
    name = Field()
    description = Field()
    link = Field()
    crawled = Field()
    spider = Field()
    url = Field()

class DmozLoader(ItemLoader):
    default_item_class = DmozItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()


class ZhihuPeopleItem(Item):
    id = Field()
    name = Field()
    sign = Field()
    location = Field()
    business = Field()
    employment = Field()
    position = Field()
    education = Field()
    education_extra = Field()
    description = Field()
    agree = Field()
    thanks = Field()
    asks = Field()
    answers = Field()
    posts = Field()
    collections = Field()
    logs = Field()
    followees = Field()
    followers = Field()
    follow_topics = Field()

