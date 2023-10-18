# pylint: disable=E1101

from googleapiclient.errors import HttpError
from pkg.calendar.service import CalendarService
from os import getenv

def create_calendar():
    cal_service = CalendarService().get_service()
    try:
        calendar_test = {
            "summary": getenv("CALENDAR_NAME")
        }
        new_calendar_response = cal_service.calendars().insert(
            body=calendar_test).execute()
        return new_calendar_response
    except HttpError as err:
        print("Cant create new calendar:", err, sep="\n")


def create_event(calendar, init_date, end_date, summary, description):
    cal_service = CalendarService().get_service()
    try:
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'date': init_date,
                'timeZone': 'America/Bogota',
            },
            'end': {
                'date': end_date,
                'timeZone': 'America/Bogota',
            },
            'reminders': {
                'useDefault': True,
            },
        }
        cal_service.events().insert(
            calendarId=calendar.get("id"), body=event).execute()

    except HttpError as error:
        print(f'An error occurred: {error}')
