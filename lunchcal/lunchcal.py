from dateutil.relativedelta import relativedelta
from icalendar import Calendar, Event

"""
File containing LunchCalendar class
"""


class LunchCalendar:
    def __init__(self, name):
        self.name = name
        self.cal = Calendar()
        self.cal.add("prodid", "-//Weekly lunch menu//{}//".format(self.name))
        self.cal.add("version", "2.0")

    def create_event(self, summary, description, start):
        """Create a 30 minute calendar event without a reminder"""
        event = Event()
        event.add("summary", summary)
        event.add("description", description)
        event.add("dtstart", start)
        event.add("dtend", start + relativedelta(minutes=30))
        event.add("dtstamp", start)
        self.cal.add_component(event)

    def write_calendar(self, filename):
        """Write calendar to an .ics file."""
        with open(filename + ".ics", "wb") as f:
            f.write(self.cal.to_ical())