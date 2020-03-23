# -*- coding: utf-8 -*-
import scrapy
import urllib
from w3lib.html import remove_tags
from ..items import ScrapyDatabaseItem


class CountrySpider(scrapy.Spider):
    items = ScrapyDatabaseItem()
    name = 'country'
    start_urls = [
        'https://travel.gc.ca/travelling/health-safety/vaccines'
    ]

    def parse(self, response):
        country = response.css('option::text')[1:].extract()
        value_tuple = response.css('option::attr(value)')[1:].extract()
        value = []
        for i in value_tuple:
            value.append(i.split(',')[0])
        for i in range(len(value)):
            path = 'https://travel.gc.ca/destinations/'+value[i]+'#health'
            nextpage = response.urljoin(path)
            yield scrapy.Request(nextpage, callback=self.vac_parse, meta={'country': country[i]})

        # yield{'country': country,'value': value}

    def vac_parse(self, response):
        items = ScrapyDatabaseItem()
        title = response.css('title::text').extract()
        vaccines = response.css('.background-light::text').extract()
        div = response.css(
            '.health-tab')[2].css('details .health-tab')
        for each in div:
            name = each.css('summary::text').extract()
            p = each.css('p,li').extract()
            details = []
            country = response.meta.get('country')
            for i in p:
                details.append(remove_tags(i))
        #name = div.css('details .background-light::text').extract()
        #detail = div.css('details p::text').extract()
            items['country'] = country
            items['name'] = name
            items['details'] = details

            yield items
