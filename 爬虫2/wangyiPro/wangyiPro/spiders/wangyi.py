# -*- coding: utf-8 -*-
import scrapy
from time import sleep
from selenium import webdriver
from wangyiPro.items import WangyiproItem
from scrapy_redis.spiders import RedisCrawlSpider
class WangyiSpider(RedisCrawlSpider):
    name = 'wangyi'
    # allowed_domains = ['news.163.com']
    # start_urls = ['https://news.163.com/']
    redis_key = 'wangyiPro'
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='/Users/tanpeng/PycharmProjects/assignment/爬虫2/chromedriver')

    def close(self, spider):
        self.bro.close()

    def parse(self, response):
        lis = response.xpath('//div[@class="ns_area list"]/ul/li')
        index_list = [3,4,6,7]
        li_list = []
        for index in index_list:
            li_list.append(lis[index])

        for li in li_list:
            url = li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/text()').extract_first()

            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=url,callback=self.parseSecond,meta={'item':item})

    def parseSecond(self,response):
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        print(len(div_list))
        item = response.meta['item']

        for div in div_list:
            url = div.xpath('./a/@href').extract_first()
            img_url = div.xpath('./a/img/@href').extract_first()
            new_title = div.xpath('./a/img/@alt').extract_first()
            item['img_url'] = img_url
            item['new_title'] = new_title
        yield item
