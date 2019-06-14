# -*- coding: utf-8 -*-
import scrapy
from moviePro.items import MovieproItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.id97.com']
    start_urls = ['http://www.id97.vip/']

    def parse(self, response):
        div_list = response.xpath('//div[@class="container"]/div[@class="row"]/div[@class="col-md-2 col-sm-6 col-xs-6 movie-item-out"]')
        for div in div_list:
            title = div.xpath('./div/a/@title').extract_first()
            time = div.xpath('.//em/strong/span/text()').extract_first()
            url = 'http://www.id97.vip'+div.xpath('./div/a/@href').extract_first()

            item = MovieproItem()

            yield scrapy.Request(url=url,callback=self.parseBySecondPage,meta={'item':item})


    def parseBySecondPage(self,response):
        div_list = response.xpath('/html/body/div[2]/div/div/div[2]/div[1]/div[2]')
        for div in div_list:
            director = div.xpath('./table/tbody/tr[1]/td[2]/text()').extract_first()
            print(director)
        item = response.meta['item']
        print('hello')

        yield item