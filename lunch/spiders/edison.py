# -*- coding: utf-8 -*-
import scrapy


class EdisonSpider(scrapy.Spider):
    name = "edison"
    allowed_domains = ["restaurangedison.se"]
    start_urls = ["http://restaurangedison.se/lunch"]
    restaurant = "Ideon Edison"

    def parse(self, response):
        weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
        for day in weekdays:
            yield {
                "weekday": day,
                "courses": response.xpath(
                    '//div[contains(@class, $val)]//descendant::div[@class="lunchmeny_container"]/div',
                    val=day,
                )
                .xpath("normalize-space(.)")
                .extract(),
            }
