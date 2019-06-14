# -*- coding: utf-8 -*-
import scrapy
from qiubaiByPages.items import QiubaibypagesItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.qiushibaike.com/text']
    start_urls = ['https://www.qiushibaike.com/text/']
    url = 'https://www.qiushibaike.com/text/page/%d/'
    PageNum = 1

    def parse(self, response):
        div_list = response.xpath('//div[@id="content-left"]/div')

        for div in div_list:
            author = div.xpath('./div[@class="author clearfix"]/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            item = QiubaibypagesItem()
            item['author'] = author
            item['content'] = content

            yield item
        if self.PageNum <= 13:
            print('爬取到了第%d页的数据'%self.PageNum)
            self.PageNum += 1
            new_url = format(self.url % self.PageNum)
            yield  scrapy.Request(url=new_url,callback=self.parse)



