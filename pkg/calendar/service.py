import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from pkg.constants import CREDENTIALS_FILE, SCOPES, TOKEN_FILE


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class CalendarService:
    __calendar_service = None

    def __create_calendar_service(self):
        credentials = self.__log_in()
        self.__calendar_service = build(
            'calendar', 'v3', credentials=credentials)

    def get_service(self):
        if self.__calendar_service is None:
            self.__create_calendar_service()
        return self.__calendar_service

    def __log_in(self):
        credentials = None
        if os.path.exists(TOKEN_FILE):
            credentials = Credentials.from_authorized_user_file(
                TOKEN_FILE, SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                credentials = flow.run_local_server(port=0)
            with open(file=TOKEN_FILE, mode='w', encoding="utf-8") as token:
                token.write(credentials.to_json())
        return credentials
