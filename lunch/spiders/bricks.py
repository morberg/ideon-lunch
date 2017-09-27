# -*- coding: utf-8 -*-
import scrapy


class BricksSpider(scrapy.Spider):
    name = 'bricks'
    allowed_domains = ['brickseatery.se']
    start_urls = ['http://brickseatery.se/lunch/']
    restaurant = 'Bricks Eatery'

    def parse(self, response):
        weekdays = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag']
        for day in weekdays:
            yield {
                'weekday': day,
                'courses': response.xpath('//div[@class="lunch"]//h3[contains(text(), $val)]/following-sibling::table[1]/tr/td[2]', val=day).xpath('normalize-space(.)').extract()
            }
