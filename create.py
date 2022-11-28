from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from oauth2client import file, client, tools
from event import *

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']
store= file.Storage('storage.json')
creds=store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run(flow, store)
service = build('calendar', 'v3', http=creds.authorize(Http()))

GMT_OFF = '+08:00'      # PDT/MST/GMT-7
EVENT = {'summary': str(x),
        'start': {
                'dateTime': str(x1) ,
                'timeZone': 'Asia/Singapore',
            },
            'end': {
                'dateTime': str(x2) ,
                'timeZone': 'Asia/Singapore',
            },}
e = service.events().insert(calendarId='primary', sendNotifications=True, body=EVENT).execute()
