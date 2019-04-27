# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    author = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    score = scrapy.Field()
    tags = scrapy.Field()
    press = scrapy.Field()
    url = scrapy.Field()
    comment_num = scrapy.Field()
    
class HistoryItem(scrapy.Item):
    url = scrapy.Field()
    date = scrapy.Field()
'''
class Author(scrapy.Item):
    name = scrapy.Field()
    introduction = scrapy.Field()
    nationality = scrapy.Field()
    sex = scrapy.Field()
    birthday = scrapy.Field()
'''
