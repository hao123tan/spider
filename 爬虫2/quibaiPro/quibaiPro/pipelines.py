# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json


class QuibaiproPipeline(object):
    coon = None
    cursor = None

    # def open_spider(self,spider):
    #
    #     self.fp = open('./qiubai_pipe.txt', 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #
    #     author = item['author']
    #     content = item['content']
    #
    #     self.fp.write(author+':'+content+'\n\n\n')
    #     return item
    #
    # def close_spider(self,spider):
    #
    #     self.fp.close()

    # def open_spider(self,spider):
    #
    #     self.coon = pymysql.connect(host='127.0.0.1',
    #                     port=3306,
    #                     user='root',
    #                     password='123',
    #                     db='qiubai'
    #                     )
    #
    # def process_item(self, item, spider):
    #     print('次数')
    #     author = item['author']
    #     content = item['content']
    #     sql = 'insert into qiubai(author, content) values("%s","%s")'%(author,content)
    #     self.cursor = self.coon.cursor()
    #     try:
    #         self.cursor.execute(sql)
    #         self.coon.commit()
    #         print('成功')
    #     except Exception as e:
    #         print(e)
    #         self.coon.rollback()
    #     return item
    #
    # def close_spider(self,spider):
    #     print('结束爬虫')
    #     self.cursor.close()
    #     self.coon.close()

    def open_spider(self, spider):
        self.coon = redis.Redis(host='127.0.0.1', port=6379)

    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        dict = {
            'author': author,
            'content': content
        }
        dict = json.dumps(dict)
        self.coon.lpush('datalist', dict)
        return item

    def close_spider(self, spider):
        print('可能结束爬虫')
        value = self.coon.lrange('datalist',0,-1)

        for i in value:
            x = json.loads(i)
            print(x)
        print('结束爬虫')
