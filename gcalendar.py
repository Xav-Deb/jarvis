from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from httplib2 import Http

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    tomorrow_tmp = datetime.datetime.today() + datetime.timedelta(days=1) #"2015-12-31T23:35:02.669052Z"
    tomorrow = tomorrow_tmp.isoformat() + 'Z' 
    #print (tomorrow)
    #print('Getting the upcoming 10 events')
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, singleEvents=True, timeMax=tomorrow, 
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    if not events:
        return('Vous n\'avez pas de rendez-vous aujourdh\'hui.')
    else:
        retour = 'Voici vos rendez-vous pour aujourdh\'hui : \n'
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        retour = retour + ('{} a {:%H:%M}'.format(event['summary'], datetime.datetime.strptime(start, '%Y-%m-%dT%H:%M:%S+01:00')))
    return retour

if __name__ == '__main__':
    main()