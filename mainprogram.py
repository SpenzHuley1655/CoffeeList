import datetime
import dateutil.parser as dp
from jsonClass import JSON

# Driver program. This is basically a template to fill in, stitching together
# all of the smaller pieces of the program from different files.

# from top to bottom, this program:

# Makes a dict from a .csv file, pairing up people from different departments
# Kevin, I'll need your part of the program (I believe it's TNY_COMMIT1.py)
# to return a simple dict. Basically, I need to be able to call a function like
# get_dict_from_csv(filename) and have it return a dict of pairings.
# Uses each pairing as parameters to the following loop:

# make a request to the Google Calendar API, with those 
# two names as parameters as well as the current date, between noon and 5pm
# pass the response object to the method described in the jsonClass file
# If the value returned by r.meeting is {}, also recognized by python as false,
# try again with the current datetime+24 hours
# repeat until you receive a response with actual entries for date and time
# iterate through this process with every pair in the original dict of pairings

# what this will look like:

"""
for key in dict_of_pairings: # <--- dict_of_pairings from Kevin's program
  response = make_google_request(key, dict_of_pairings[key], current_date) #design make_google_request
  r = JSON(response)
  r.do_all()
  while not r.meeting: # an empty dict corresponds to "false" in python. 
    make_google_request(key, dict_of_pairings[key], next_weekday) #must design next_weekday
    r = JSON(response)
    r.do_all()
    
  # then, use the Google Calendar API to create an event on those two peoples 
  # calendars.
  make_event(r.email1, r.email2, r.meeting['start'], r.meeting['end']) #must design make_event
  
"""


# There are two functions that must be designed here to interact with Google Calendar
# The first, make_google_request, in line 28, requires use of the freebusy() module mentioned in the Developer Docs. 
# https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.freebusy.html

# The second, make_event, which I believe will be easier, requires the insert event method, also through the Google Calendar API.
# https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/calendar_v3.events.html#insert

# I know this is kind of murky, please call/email me and I can walk you through setting up the API. 

