import datetime
from quickstart import get_calendar_service
import webbrowser

def main():
    service = get_calendar_service()
    print('Getting List o 10 events')
    # Call the Calendar API
    while 1:
        now = datetime.datetime.now().isoformat().split('.')[0] + '+05:30' # 'Z' indicates UTC time
        events_result = service.events().list(
            calendarId='primary', timeMin=now,
            maxResults=10, singleEvents=True,
            orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            if now == start:
                print(start, event['summary'])
                webbrowser.open(event['location'])
if __name__ == '__main__':
   main()