# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import records
import re
import MySQLdb

class DoubanBookPipeline(object):
    def __init__(self):
        self.db = records.Database("mysql://scrapy:12345678@localhost/douban_book",
                                   connect_args = {'charset':'utf8'})
        self.price_re = re.compile("\d+\.?\d+")
        query = '''
        CREATE TABLE IF NOT EXISTS book 
        (
            id int(11) AUTO_INCREMENT,
            author varchar(50) NOT NULL,
            book_name varchar(60) NOT NULL,
            year date,
            price decimal(6,2),
            score decimal(2,1),
            tags varchar(60),
            press varchar(60),
            url text NOT NULL,
            comment_num varchar(50),
            PRIMARY KEY(id)            
        )DEFAULT CHARSET=utf8;
        '''
        self.db.query(query)

    def process_item(self, item, spider):
        #print(item)
        query = '''
            INSERT INTO book (book_name,author,year,price,score,tags,press,url,comment_num) 
            VALUES 
            ('%s','%s','%s-1','%s','%s','%s','%s','%s','%s');
        '''%(item['book_name'],
             item['author'],
             item['year'],
             item['price'],
             item['score'],
             item['tags'],
             item['press'],
             item['url'],
             item['comment_num'])
        try:
            self.db.query(query)
        except MySQLdb._exceptions.OperationalError:
            print("录入%s信息时数据错误"%(item['book_name']))
        return item
