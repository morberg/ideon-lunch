# -*- coding: utf-8 -*-
import scrapy


class EdisonSpider(scrapy.Spider):
    name = 'edison'
    allowed_domains = ['restaurangedison.se']
    start_urls = ['http://restaurangedison.se/lunch']
    restaurant = 'Ideon Edison'

    def parse(self, response):
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        menu = {}
        for day in weekdays:
            yield {
                'weekday': day,
                'courses': response.xpath('//div[@id=$val]/table//td[@class="course_description"]/p/text()', val=day).extract()
            }