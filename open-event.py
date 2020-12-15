import datetime
from quickstart import get_calendar_service
import webbrowser

def main():
    # Call the Calendar API
    service = get_calendar_service()

    while 1:

        now = datetime.datetime.now().isoformat().split('.')[0] + '+05:30' # 'Z' indicates UTC time

        events_result = service.events().list( calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()

        events = events_result.get('items', [])

        if not events:
            continue

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            if now == start or now == start[:17]+'01' or now == start[:17]+'02':
                print(start, "Opening" ,event['summary'])
                webbrowser.open_new(event['location'])

if __name__ == '__main__':
    main()