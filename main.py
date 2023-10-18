# pylint: disable=E1101

from pkg.calendar import createCalendar, createEvent
from pkg.unir.read import read_events

def main():
    events = read_events()

if __name__ == '__main__':
    main()
