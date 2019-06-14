# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from doubanPro.spiders.new_selenium import get_url


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    bro = webdriver.Chrome(executable_path='/Users/tanpeng/PycharmProjects/assignment/爬虫2/chromedriver')
    # allowed_domains = ['www.douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']
    def start_requests(self):
        for url in self.start_urls:
            page_source = get_url(self.bro,url)
            fp = open('second_main.html', 'w', encoding='utf-8')
            fp.write(page_source)
        self.bro.close()


    # def parseBySecondPage(self,response):
    #     fp = open('second_main.html', 'w', encoding='utf-8')
    #     fp.write(response.text)
    #     self.bro.close()

    def parse(self, response):
        # fp = open('main.html','w',encoding='utf-8')
        # fp.write(response.text)
        # self.bro.close()
        # url = 'https://www.douban.com/people/188951058/'
        # yield scrapy.Request(url=url,callback=self.parseBySecondPage)
        pass
