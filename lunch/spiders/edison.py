# -*- coding: utf-8 -*-
import scrapy


class EdisonSpider(scrapy.Spider):
    name = 'edison'
    allowed_domains = ['restaurangedison.se']
    start_urls = ['http://restaurangedison.se/lunch']

    def parse(self, response):
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        menu = {}
        for day in weekdays:
            yield {
                'restaurant': 'Ideon Edison',
                'weekday': day,
                'courses': response.xpath('//div[@id=$val]/table//td[@class="course_description"]/p/text()', val=day).extract()
            }
