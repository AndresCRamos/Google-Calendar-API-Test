from constants import CALENDAR_NAME, CREDENTIALS_FILE, SCOPES, TOKEN_FILE

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def logIn():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    credentials = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        credentials = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(file=TOKEN_FILE, mode='w', encoding="utf-8") as token:
            token.write(credentials.to_json())
    return credentials

def createCalendarService(credentials):
    return build('calendar', 'v3', credentials=credentials)

def createCalendar(calendar_service):
    try:
        calendar_test = {
            "summary": CALENDAR_NAME
        }
        new_calendar_response = calendar_service.calendars().insert(body=calendar_test).execute()
        return new_calendar_response
    except HttpError as err:
        print("Cant create new calendar:", err, sep="\n")

def createEvent(cal_service, calendar, init_date, end_date, summary, description):
    try:
        event = {
            'summary': summary,
            'description': description,
            'start': {
                'dateTime': init_date,
                'timeZone': 'America/Bogota',
            },
            'end': {
                'dateTime': end_date,
                'timeZone': 'America/Bogota',
            },
            'reminders': {
                'useDefault': True,
            },
        }
        event_result = cal_service.events().insert(calendarId=calendar.get("id"), body=event).execute()
        print(event_result)

    except HttpError as error:
        print(f'An error occurred: {error}')
