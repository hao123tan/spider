# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from redisPro.items import RedisproItem
from scrapy_redis.spiders import RedisCrawlSpider


class QiubaiSpider(RedisCrawlSpider):
    name = 'qiubai'
    # allowed_domains = ['www.qiushibaike.com/pic/']
    # start_urls = ['http://www.qiushibaike.com/pic//']
    redis_key = 'qiubaispider'
    link = LinkExtractor(allow=r'/pic/page/\d+?')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            img_url = 'https:' + div.xpath('.//div[@class="thumb"]/a/img/@src').extract_first()

            item = RedisproItem()
            item['img_url'] = img_url

            yield item