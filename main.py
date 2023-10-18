# pylint: disable=no-member
from pkg.calendar import createCalendar, createEvent, logIn, createCalendarService

def main():
    credentials = logIn()
    cal_service = createCalendarService(credentials)
    new_calendar_response = createCalendar(cal_service)
    createEvent(
        cal_service=cal_service,
        calendar=new_calendar_response,
        init_date="2023-10-17T17:00:00",
        end_date="2023-10-17T17:30:00",
        summary="Test Event",
        description="Custom description"
    )


if __name__ == '__main__':
    main()
