# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals


class MyProxy(object):
    def process_request(self,request,spider):
        request.meta['proxy'] = '14.20.235.201:9797'