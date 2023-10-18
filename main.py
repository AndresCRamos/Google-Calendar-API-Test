# pylint: disable=E1101
from pkg.calendar.calendar import create_calendar, create_event
from pkg.unir.read import read_events

def main():
    events = read_events()
    calendar = create_calendar()
    for event in events:
        create_event(calendar=calendar, **event)

if __name__ == '__main__':
    main()
