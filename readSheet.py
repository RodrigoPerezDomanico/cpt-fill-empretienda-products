from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def _pointManager(values):
    unpointed_values=[]
    for value in values:
        new_price=int(str(value[1]).replace('.','').replace('$',''))
        unpointed_values.append([value[0],new_price,value[2]])

    return unpointed_values



def getNewValues():
    SPREADSHEET_ID = '115MlBOna5noGZRmpdGrY6cm1wOf8xlJQZFHABcINNP0'
    RANGE_NAME ='Hoja 1!A2:C'
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                    range=RANGE_NAME).execute()
        values = result.get('values', [])
        if not values:
            print('No data found.')
            return

        # print('Name, Major:')
        # print (values)
        unpointed_values=_pointManager(values)
        return unpointed_values
        
    except HttpError as err:
        print(err)

# Values=getNewValues()
# print(Values[0])