# -*- coding:utf-8 -*-

"""
@version: python2.7
@author: ‘zhangdf‘
@license: Apache Licence 
@contact: 2921558948@qq.com
@site: 
@software: PyCharm
@file: author_spider.py
@time: 2019/2/16 10:10
"""

import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a:attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
            'location': extract_with_css('.author-born-location::text'),
        }