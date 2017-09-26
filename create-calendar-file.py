#!/usr/local/bin/python3
import json
from lunchcal.lunchcal import LunchCalendar
from datetime import *; from dateutil.relativedelta import *

def cal(restaurant='Ideon Edison'):
    """Create an .ics file with a restaurant's weekly menu
    
    :param restaurant: The restaurant of choice
    """
    with open('lunch.json') as f:
        menu = json.load(f)
    lunch_calendar = LunchCalendar(restaurant)
    # First lunch_date is 11:30 on Monday of current week    
    lunch_date = datetime.now().replace(hour=11,minute=30) + relativedelta(weekday=MO(-1))
    for daily_menu in menu:
        courses = ''
        for item in daily_menu['courses']:
            courses = courses + item + '\n\n' 
        lunch_calendar.create_event(restaurant, courses, lunch_date)
        lunch_date = lunch_date + relativedelta(days=1)
    lunch_calendar.write_calendar(restaurant)
    
if __name__ == '__main__':
    cal()