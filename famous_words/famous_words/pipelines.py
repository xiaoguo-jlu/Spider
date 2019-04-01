# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import records

class FamousWordsPipeline(object):
    # connect_args参数是个巨坑。。。
    def __init__(self):
        self.db = records.Database("mysql://scrapy:12345678@localhost/famous_words",
                                   connect_args = {'charset':'utf8'})

    def process_item(self, item, spider):
        query = '''
        INSERT INTO words (author,words,tags) VALUES ('%s','%s','%s');
        '''%(item['author'],item['words'],item['tags'])
        rows = self.db.query(query)
        #('利国','liguo','liguo')
#            ("'liguo'","'liguo'","'liguo'")
