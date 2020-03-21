# -*- coding: utf-8 -*-
import scrapy
import urllib


class CountrySpider(scrapy.Spider):
    name = 'country'
    allowed_domains = ['https://travel.gc.ca/']
    start_urls = [
        'https://travel.gc.ca/travelling/health-safety/vaccines']

    def parse(self, response):
        selectors = response.xpath('//details/details/summary').extract()
        # print(selectors)
        namelist = response.xpath('//details/details/summary').extract()
        detaillist = response.xpath("//details/details/").extract()
        listlength = len(namelist)
        item = {}
        for i in range(0, listlength):
            item['Name'] = namelist[i]
            item['Vaccine'] = htmllist[i]

            urllib.request.urlretrieve(
                "https://travel.gc.ca/destinations/"+str(list[i]))
            yield item
