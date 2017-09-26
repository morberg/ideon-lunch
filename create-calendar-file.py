#!/usr/local/bin/python3

import json
from icalendar import Calendar, Event, Alarm, vText
from datetime import *; from dateutil.relativedelta import *
from dateutil.relativedelta import relativedelta 
import calendar

menu_file = 'lunch.json'

def create_calendar(restaurant):
    cal = Calendar()
    cal.add('prodid', '-//Weekly lunch menu//{}//'.format(restaurant))
    cal.add('version', '2.0')
    return cal

def create_event(cal, summary, description, start):
    """Create a calendar event between 11.30-12.00 without a reminder"""
    event = Event()
    no_alarm = Alarm()
    event.add('summary', summary)
    event.add('description', description)
    event.add('dtstart', start)
    event.add('dtend', start + relativedelta(minutes=30))
    event.add('dtstamp', start)
#    event.add('location', location)
    no_alarm.add('action', 'NONE')
    no_alarm.add('trigger', start - relativedelta(years=1)) # Set an alarm date before the event to remove reminder
    event.add_component(no_alarm)
    cal.add_component(event)

def write_calendar(cal, filename):
    with open(filename + '.ics', 'wb') as f:
        f.write(cal.to_ical())

def cal(restaurant='Ideon Edison'):
    """Create an .ics file with a restaurant's weekly menu
    
    :param restaurant: The restaurant of choice
    """
    with open(menu_file) as f:
        menu = json.load(f)
    cal = create_calendar(restaurant)
    # First lunch_date is 11:30 on Monday of current week    
    lunch_date = datetime.now().replace(hour=11,minute=30) - relativedelta(weekday=MO)
    for daily_menu in menu:
        courses = ''
        for item in daily_menu['courses']:
            courses = courses + item + '\n\n' 
        create_event(cal, restaurant, courses, lunch_date)
        lunch_date = lunch_date + relativedelta(days=1)
    write_calendar(cal, restaurant)
    
if __name__ == '__main__':
    cal()