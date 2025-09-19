from icalendar import Calendar, Event
from pytz import UTC

def create_ics(date_start, date_end, summary="Event"):
    cal = Calendar()
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', date_start.replace(tzinfo=UTC))
    if date_end:
        event.add('dtend', date_end.replace(tzinfo=UTC))
    cal.add_component(event)

    with open('event.ics', 'wb') as f:
        f.write(cal.to_ical())
