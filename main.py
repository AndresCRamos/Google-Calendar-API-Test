#pylint: disable=no-member
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
TOKEN_FILE = ".token.json"
CREDENTIALS_FILE = ".google-oauth2_credentials.json"
CALENDAR_NAME = "calendario de test"



def main():
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

    try:
        cal_service = build('calendar', 'v3', credentials=credentials)
        calendar_test = {
            "summary": "Nuevo calendario de test"
        }
        response = cal_service.calendars().insert(body = calendar_test).execute()
        print(response)

    except HttpError as error:
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()
