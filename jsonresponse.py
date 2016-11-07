import datetime
import dateutil.parser as dp

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

def main(responseobject):
    email1 = fetch_email_1(responseobject)
    email2 = fetch_email_2(responseobject)
    m = json_handler(responseobject, email1, email2)
    print m
    return

# Dict -> string  
# extract the first email from the jsonobject
def fetch_email_1(ajson):
    email = ajson['calendars'].keys()[0]
    return email

def fetch_email_2(ajson):
    email = ajson['calendars'].keys()[1]
    return email 
# JSON Object -> Datetime
# Find a 30 minute block of time when the people are free to meet
def json_handler(a_json, email1, email2):
    busy_object1 = get_busy(a_json, email1)
    busy_object2 = get_busy(a_json, email2)
    meet_time = find_free(busy_object1, busy_object2)
    return meet_time

# JSON String -> List
# Retrieve the list containing all of the start/end times for user's busy block
def get_busy(a_json, email):
    busy_object = a_json['calendars'][email]['busy']
    return busy_object

# list -> string
# return the nth element of a list
def get_nth_busy(a_list,n):
    return a_list[n]

# [list-of dict] [list-of dict] -> dict
# iterate through each list,
# checking to see if there are non-overlapping windows of free time
def find_free(obj1, obj2):
    meeting = {}
    for x in range(0, len(obj1)):
        for y in range(0, len(obj2)):
            if is_room(get_nth_busy(obj1, x), get_nth_busy(obj2, y)):
                print "Found meeting time!"
                print x
                print y
                meeting['start'] = retrieve_start(obj1[x], obj2[y])
                meeting['end'] = retrieve_end(meeting['start'])
                break
    return meeting

# dict dict -> Boolean
# is there room for a 30 minute meeting between these two dicts?
def is_room(obj1, obj2):
    t = datetime.timedelta(minutes=30)
    b1 = dp.parse(obj1['start']) <= dp.parse(obj2['end']) + t
    b2 = dp.parse(obj1['end']) + t >= dp.parse(obj2['start'])
    b = b1 & b2
    return not b

# dict dict -> Datetime
# get start time of meeting
def retrieve_start(obj1, obj2):
    if dp.parse(obj2['start']) > dp.parse(obj1['end']):
        start_time = dp.parse(obj1['end'])
    else:
        start_time = dp.parse(obj2['end'])
    return start_time

# dict dict -> Datetime
# get end time of meeting
def retrieve_end(start):
    end = start + datetime.timedelta(minutes=30)
    return end

if __name__ == '__main__':
    main(responseobject2)

