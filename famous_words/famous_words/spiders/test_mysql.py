import records

db = records.Database('mysql://scrapy:12345678@localhost/famous_words')
query = '''
    create table if not exists words
    (
        id int(11) AUTO_INCREMENT,
        author char(20),
        words text NOT NULL,
        tags char(50),
        PRIMARY KEY(id)
    ) DEFAULT CHARSET=utf8;   
    '''
rows = db.query(query)
query = "SHOW TABLES;"
rows = db.query(query)

for row in rows:
    print(row)
