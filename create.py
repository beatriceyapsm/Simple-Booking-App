from __future__ import print_function

import datetime
import os.path
import os

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

# Get environment variables
REFRESHTOKEN= os.environ.get("REFRESHTOKEN")
CLIENTID= os.environ.get("CLIENTID")
CLIENTSECRET= os.environ.get("CLIENTSECRET")
SCOPES = ['https://www.googleapis.com/auth/calendar']
creds = Credentials("",refresh_token=REFRESHTOKEN, token_uri ="https://oauth2.googleapis.com/token", client_id= CLIENTID , client_secret=CLIENTSECRET, scopes=SCOPES)
service = build('calendar', 'v3', credentials=creds)

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
