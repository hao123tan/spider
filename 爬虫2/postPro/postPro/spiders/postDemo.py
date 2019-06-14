# -*- coding: utf-8 -*-
import scrapy


class PostdemoSpider(scrapy.Spider):
    name = 'postDemo'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']
    def start_requests(self):
        data = {
            'kw':'dog'
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)

    def parse(self, response):
        print(response.text)