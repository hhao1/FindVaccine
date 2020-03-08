# -*- coding: utf-8 -*-
import scrapy


class CountrySpider(scrapy.Spider):
    name = 'country'
    allowed_domains = ['https://travel.gc.ca/']
    start_urls = [
        'https://travel.gc.ca/destinations/afghanistan#health']

    def parse(self, response):
        selectors = response.xpath('//details/details/summary')
        print(selectors)
