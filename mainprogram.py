import datetime
import dateutil.parser as dp
from jsonClass import JSON

# Driver program. This is basically a template to fill in, stitching together
# all of the smaller pieces of the program from different files.

# from top to bottom, this program:
# Makes a dict from a .csv file, pairing up people from different departments
# Uses each pairing as parameters to the following loop:

# make a request to the Google Calendar API, with those 
# two names as parameters as well as the current date, between noon and 5pm
# pass the response object to the method described in the jsonClass file
# If the value returned by r.meeting is {}, also recognized by python as false,
# try again with the current datetime+24 hours
# repeat until you receive a response with actual entries for date and time

# then, use the Google Calendar API to create an event on those two peoples 
# calendars.

# iterate through this process with every pair in the original dict of pairings
