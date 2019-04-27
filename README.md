# Spider
__scrapy数据挖掘日常__
## 说明
除了.idea文件夹以外，每个文件夹对应于一个scrapy爬虫项目 <br/>
### 环境
IDE：pycharm <br/>
操作系统：Ubuntu 16.04 <br/>
数据库：Mysql5.7 <br/>
python版本：python3.5，依赖records库

## 运行
运行爬虫之前，需要先建立一个mysql数据库用户，用户名为scrapy，密码为12345678，同时还需建立一个与工程名相同的数据库：
    
    #创建用户
    create user 'srcapy'@'localhost' identified by '12345678';
    #分配查询和插入数据的权限
    grant select,insert on famous_words.* to 'scrapy'@'localhost';

建立了数据库后，进入对于爬虫项目文件夹下，使用scrapy crawl 爬虫名即可运行爬虫，如

    scrapy crawl famous_words
爬虫名是spiders文件夹中，继承了scrapy.Spider类的自定义类所对应的name属性
我在起名时，都以项目名作为爬虫名

## 当前所有项目
|项目名|网站|数据|描述|日期|
|-|-|-|-|-|
|famous_words|[lab.scrapyd.cn](http://lab.scrapyd.cn)|名言|学习过程中的第一只scrapy爬虫|2019-4-8|
|douban_book|[豆瓣图书](https://book.douban.com)|图书信息|根据标签进行爬取，爬取字段有作者，价格，评分等信息|2019-4-26|

