import scrapy
import os
from famous_words.items import FamousWordsItem

class famous_words(scrapy.Spider):
    name = "famous_words"
    start_urls = ["http://lab.scrapyd.cn/page/1"]

    def parse(self, response):
        divs = response.css('.quote.post')
        data_dir = os.getcwd() + "/data/"
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)
        file_name = data_dir + "Page " + response.url.split("/")[-2]

        for i in divs:
            item = FamousWordsItem()
            item['author'] = i.css(".author::text").extract_first()
            item['words'] = i.css(".text::text").extract_first()
            item['tags'] = ",".join(i.css(".tag::text").extract())
            yield item

        next_page_url = response.css('.page-navigator').css('.next a::attr(href)').extract_first()
        if next_page_url:
            yield scrapy.Request(url = next_page_url, callback = self.parse)