import datetime
import dateutil.parser as dp
"""
Kevin/Chris/whoever:

Hi! This is a useful class implementation of how to actually retrieve a 
meeting time for two people. It was complicated enough getting it to work
for two people, so it looks like whenever there's a group of three, they'll just
have to figure it out themselves. The code doesn't really work otherwise. 

The way to make this work is to call it using an external function. The idea
is that, by calling an as-yet-to-be-solved function that utilizes the 
Google Calendar API, we can give Google Calendar two emails, and a time slot,
and this will return a JSONObject. The format of this JSONObject will look like
the examples below: responseobject1 and responseobject2. This is a python dict.

The code below will attempt to find a meeting time, using the two emails and time
slot given. Remember that in the grand scheme of things, the responseobject is
passed to this function by using an external function (the google calendar api)
to get a response object. Then, we do this:

from jsonClass import JSON

r = JSON(name-of-response-object-here)
r.do_all() # assigns values to essential aspects of the response object

# r.meeting <--- returns a dict with either two datetime objects, start and end,
# or an empty dict. AN EMPTY DICT SIGNIFIES THAT NO VALID TIME TO MEET WAS FOUND.
# the idea is that the function in the main algorithm, which calls the r.do_all()
# method on the given response object, will either return a 30 minute window
# in which the two people can meet, or an empty dict. If it is an empty dict,
# we re-call the function to get a response object from the Google Calendar,
# but move the date and time one day into the future. We keep doing this until
# we get a non-empty-dict response object

-------------------------------
Potential bugs:
-fetch_emails() seems to return the emails, but switched.
Not sure if I'm incorrectly indexing the calendars. 
-I hard coded a method by which, if both people have nothing on their calendars
for this particular day, r.meeting['start'] will have the value 'noon',
and r.meeting['end'] will have the value '12:30'. These are not valid datetime
objects, and the idea is that, if this method returns these values, the main 
algorithm would have to use the date that it gave the Google Calendar function
as a way to transform 'noon' and '12:30' into appropriate datetime objects
for that particular date. This MUST be addressed.

Please let me know if any of this is unclear, I still compulsively check my
email. spencer.hurley99@gmail.com
"""
responseobject2  = {
    "kind": "calendar#freeBusy",
    "timeMin": "2016-10-28T04:00:00.000Z",
    "timeMax": "2016-10-29T04:00:00.000Z",
    "calendars": {
        "kevink@ellevationeducation.com": {
            "busy": []
        },
        "spencerh@ellevationeducation.com": {
            "busy": [
                {
                    "start": "2016-10-28T20:30:00Z",
                    "end": "2016-10-28T21:30:00Z"
                }
            ]
        }
    }
}

responseobject1 = {
    "kind": "calendar#freeBusy",
    "timeMin": "2016-10-28T04:00:00.000Z",
    "timeMax": "2016-10-29T04:00:00.000Z",
    "calendars": {
        "kevink@ellevationeducation.com": {
            "busy": [
                {
                    "start": "2016-10-28T13:30:00Z",
                    "end": "2016-10-28T14:20:00Z"
                },
                {
                    "start": "2016-10-28T15:00:00Z",
                    "end": "2016-10-28T15:30:00Z"
                },
                {
                    "start": "2016-10-28T19:30:00Z",
                    "end": "2016-10-28T20:20:00Z"
                },
                {
                    "start": "2016-10-28T20:30:00Z",
                    "end": "2016-10-28T21:30:00Z"
                }
            ]
        },
        "spencerh@ellevationeducation.com": {
            "busy": [
                {
                    "start": "2016-10-28T20:30:00Z",
                    "end": "2016-10-28T21:30:00Z"
                }
            ]
        }
    }
}
#------------------------------------------------------------------------------
class JSON(object):
    
    def __init__(self, jsonobject):
        self.json = jsonobject
        self.meeting = {}
        
    
    # json -> string
    # Create entries for email1 and email2 by parsing elements of the json obj
    def fetch_emails(self):
        self.email1 = self.json['calendars'].keys()[0]
        self.email2 = self.json['calendars'].keys()[1]
    
    # create "busy objects", which are lists of dicts
    # to be used to get meeting times
    def get_busy_objects(self):
        self.busy_obj1 = self.json['calendars'][self.email1]['busy']
        self.busy_obj2 = self.json['calendars'][self.email2]['busy']
        
    # Can we assume that both people are busy
    # or is this a different situation?
    def set_pivot(self):
        if len(self.busy_obj1) == 0 & len(self.busy_obj2) == 0:
            self.pivot = 0
        elif len(self.busy_obj1) == 0:
            self.pivot = 1
        elif len(self.busy_obj2) == 0:
            self.pivot = 2
        else:
            self.pivot = 3
    
    # Determine the start and end time of the meeting
    def find_free(self):
        if self.pivot == 0:
            self.meeting['start'] = 'noon'
            self.meeting['end'] = '12:30'
        elif self.pivot == 1:
            self.one_empty(self.busy_obj1, self.email1)
        elif self.pivot == 2:
            self.one_empty(self.busy_obj2, self.email2)
        else:
            self.normal_meeting()
   
    #use in the case of there being one empty calendar         
    def one_empty(self, obj, email):
        busy_list = self.json['calendars'][email]['busy']
        if len(busy_list) == 1:
            self.meeting['start'] = dp.parse(obj[0]['end'])
            self.meeting['end'] = self.retrieve_end(self.meeting['start'])
        else:
            for x in range(0, len(busy_list) - 1):
                self.meeting['start'] = self.retrieve_start(obj[x], obj[x+1])
                self.meeting['end'] = self.retrieve_end(self.meeting['start'])
    
    # If both people have events on their calendars, use this method to
    # determine the time that they should meet
    # self.meeting is a dict with start and end keys, both of which are
    # datetime objects
    def normal_meeting(self):
        for x in range(0, len(self.busy_obj1)):
            for y in range(0, len(self.busy_obj2)):
                if is_room(self.busy_obj1[x], self.busy_obj2[y]):
                    self.meeting['start'] = self.retrieve_start(self.busy_obj1[x], self.busy_obj2[y])
                    self.meeting['end'] = self.retrieve_end(self.meeting['start'])
    
        
    # dict dict -> Datetime
    # get start time of meeting
    def retrieve_start(self,obj1, obj2):
        if dp.parse(obj2['start']) > dp.parse(obj1['end']):
            start_time = dp.parse(obj1['end'])
        else:
            start_time = dp.parse(obj2['end'])
        return start_time
    
    # add 30 minutes to end time and set as meeting end
    def retrieve_end(self,start):
        end = start + datetime.timedelta(minutes = 30)
        return end
    
    def do_all(self):
        self.fetch_emails()
        self.get_busy_objects()
        self.set_pivot()
        self.find_free()
        print self.meeting


# [List-of Dict] [List-of Dict] -> Dict
# determine whether one or both of the calendars are empty
def busy_status(obj1, obj2):
    if len(obj1) == 0 & len(obj2) == 0:
        indicator = 0 
    elif len(obj1) == 0:
        indicator = 1
    elif len(obj2) == 0:
        indicator = 2
    else:
        indicator = 3
    return indicator

# dict dict -> Boolean
    # is there room for a 30 minute meeting between these two dicts?
def is_room(obj1, obj2):
    t = datetime.timedelta(minutes=30)
    b1 = dp.parse(obj1['start']) <= dp.parse(obj2['end']) + t
    b2 = dp.parse(obj1['end']) + t >= dp.parse(obj2['start'])
    b = b1 & b2
    return not b
if __name__ == '__main__':
    r = JSON(responseobject1)
    r.do_all()

