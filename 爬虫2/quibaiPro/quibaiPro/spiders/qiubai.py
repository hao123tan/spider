# -*- coding: utf-8 -*-
import scrapy
from quibaiPro.items import QuibaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')
        for div in div_list:
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()


            item = QuibaiproItem()
            item['author'] = author
            item['content'] = content

            yield item

