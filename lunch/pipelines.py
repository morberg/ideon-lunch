# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from lunchcal.lunchcal import LunchCalendar
from datetime import *; from dateutil.relativedelta import *

class LunchPipeline(object):
    """Creates an .ics file with five daily entries, Monday-Friday."""
    def open_spider(self, spider):
        spider.log('Open Lunch Spider: {}'.format(spider.name), logging.INFO)
        self.cal = LunchCalendar(spider.name)
        # First lunch_date is 11:30 on Monday of current week    
        self.lunch_date = datetime.now().replace(hour=11,minute=30) + relativedelta(weekday=MO(-1))

    def close_spider(self, spider):
        spider.log('Creating calendar file: {}.ics'.format(spider.name), logging.INFO)
        self.cal.write_calendar(spider.name)

    def process_item(self, item, spider):
#        spider.log(item['weekday'], self.lunch_date)
        courses = ''
        for course in item['courses']:
            courses = courses + course + '\n\n' 
        self.cal.create_event(spider.restaurant, courses, self.lunch_date)        
        self.lunch_date = self.lunch_date + relativedelta(days=1)
        return item