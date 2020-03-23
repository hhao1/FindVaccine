import scrapy
from w3lib.html import remove_tags
from ..items import ScrapyDatabaseItem


class VaccineSqider(scrapy.Spider):
    name = 'vaccines'
    start_urls = [
        'https://travel.gc.ca/destinations/australia#health'
    ]

    def parse(self, response):
        items = ScrapyDatabaseItem()
        title = response.css('title::text').extract()
        vaccines = response.css('.background-light::text').extract()
        div = response.css(
            '.health-tab')[2].css('details .health-tab')
        for each in div:
            name = each.css('summary::text').extract()
            p = each.css('p,li').extract()
            details = []
            for i in p:
                details.append(remove_tags(i))
        #name = div.css('details .background-light::text').extract()
        #detail = div.css('details p::text').extract()
            items['name'] = name
            items['details'] = details
            yield items
