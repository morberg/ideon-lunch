# -*- coding: utf-8 -*-
import scrapy


class FinnSpider(scrapy.Spider):
    name = 'finn'
    allowed_domains = ['www.finninn.se/lunch-meny/']
    start_urls = ['http://www.finninn.se/lunch-meny/']
    restaurant = "Finn Inn"

    def parse(self, response):
        weekdays = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']
        for day in weekdays:
            yield {
                'weekday': day,
                'courses': response.xpath('//div[@class="grid2column"][contains(text(), $val)]/following-sibling::div[@class="item-description-menu"]', val=day).xpath('normalize-space(.)').extract()
            }
