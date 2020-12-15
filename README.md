# Automated Event Link Opener

This project is made using Python3.

### Libraries used: 
  1. Google Client Library
  2. Web Browser
  3. Pickle
  4. Date Time
  
### Working of auth.py
  The `datetime` library is used to check if the credentials are still valid or not.
  The `pickle` library is used to generate the `token.pickle` file which is created after the application is granted access to the calendar.
  The `os.path` library is used to check for the existance of token.pickle file.
  The Google Client Libraries are used for OAuth, and getting the services.

### Working of open-event.py
  This is a forever running program, which updates time, fetches new events, and also opens the event at the right time with just a second or 2 delay.
  The `now` variable is used to update the time.
      The `'+05:30'` represents the Time Zone of the country.
  <br>
  The `events_result` gets the events from the calendar.
  The `events` variable gets the list of events from the `events_result` variable.
  <br>
  Now, if the events variable doesn't contain any events, the loop executes again from the start.
  And, if the events variable contains events, the `start` variable stores the time at which the event occurs.
       Now, the if statement checks if the time now is the same as the time at which the event starts. The 2 extra conditions check if now is equal to the first seconds of the          event start time, as the execution time of the loop may vary.
  So, when the condition becomes true, the start time, and the event name are printed in the terminal, and with the help of webbrowser library, we open the link of the event, using event['location']. 
