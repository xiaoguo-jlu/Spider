# -*- coding: utf-8 -*-
import scrapy
import time
import re
import random
from douban_book.items import DoubanBookItem

class DoubanBookSpiderSpider(scrapy.Spider):
    name = 'douban_book_spider'

    def __init__(self):
        self.price_re = re.compile("\d+\.\d+")
        self.score_re = re.compile("\d+\.?\d+")
        self.year_re = re.compile("\d{4}-\d{1,2}")
        self.num_re = re.compile("\d+")
        self.press_re = re.compile("\w*出版\w*")
        self.debug_flag = True
        self.all_tags_url = []

    def start_requests(self):
        start_urls = ['https://book.douban.com/']
        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse_more_tags)

    def parse(self, response):
        infos = response.css("div.info")
        title = response.css("title::text").extract_first().replace("\n","").replace(" ","").split("/")[0].split(":")[-1]
        for info in infos:
            item = DoubanBookItem(press="未知出版社",year="1000-1",price="0.00",comment_num="0",score="0.0")
            item['tags'] = title
            item['book_name'] = info.css("a::attr(title)").extract_first()
            item['url'] = info.css("a::attr(href)").extract_first()
            data = info.css(".pub::text").extract_first().replace("\n","").replace(" ","")
            item['author'] = data.split('/')[0]
            item['score'] = info.css(".star.clearfix").css(".rating_nums::text").extract_first()
            item['comment_num'] = info.css(".star.clearfix").css(".pl::text").extract_first().replace("\n","").replace(" ","")
            try:
                item['price'] = self.price_re.search(data).group(0)
                item['year'] = self.year_re.search(data).group(0)
                item['press'] = self.press_re.search(data).group(0)
                item['comment_num'] = self.num_re.search(item['comment_num']).group(0)
                item['score'] = self.score_re.search(item['score']).group(0)
            except AttributeError:
                print(item['book_name'] + "资料丢失!")
            except TypeError:
                print(item['book_name'] + "缺少键值")
            finally:
                yield item
        next_url = response.css(".paginator").css(".next a::attr(href)").extract_first()
        if next_url:
            time.sleep(random.random()*2+1)
            yield scrapy.Request(self.join_url(next_url),callback=self.parse)
        else:
            yield scrapy.Request(self.all_tags_url[0],callback=self.parse)
            self.all_tags_url.pop(0)

    def parse_more_tags(self,response):
        more_tags_url = self.join_url(response.css(".tag.more_tag").css('a::attr(href)').extract_first())
        yield scrapy.Request(more_tags_url,callback=self.parse_all_tags)

    def parse_all_tags(self,response):
        all_tags = response.css(".tagCol").css("td a::attr(href)").extract()
        self.all_tags_url = [self.join_url(i) for i in all_tags]
        yield scrapy.Request(self.all_tags_url[0],callback=self.parse)
        self.all_tags_url.pop(0)

    def join_url(self,url):
        url = "https://book.douban.com" + url;
        return url

    def show_result(self,result_list):
        for i in result_list:
            print(i)

'''
    def parse_book(self,response):
        item = DoubanBookItem()
        item['book_name'] = response.css("#wrapper").css("h1").css("span::text").extract_first()
        info = response.css("div#info").css("span.pl::text")
        print(info)
        info = response.css("div#info").css("br::text")
        print(info)
        item['author'] = response.css("div#info").css("a::text").extract_first()
        item['press'] = response.css("div")
'''
