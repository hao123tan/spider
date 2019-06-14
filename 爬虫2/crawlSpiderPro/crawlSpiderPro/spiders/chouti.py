# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    # allowed_domains = ['dig.chouti.com']
    start_urls = ['https://dig.chouti.com/']
    link = LinkExtractor(allow=r'/all/hot/recent/\d+')
    rules = (
        Rule(link, callback='parse_item', follow=False),
    )

    def parse_item(self, response):
       author = response.xpath('//*[@id="content-list"]/div/div[4]/div[2]/a[4]/b/text()').extract_first()
       print(author)

