import pandas as pd
import random

df = []
filename = 'Employees_Birthday_Report_FINAL.csv'

def create_initial_list(filename):
    """
    Inputs a .csv filename
    returns a list of full names from the file
    """
    df = pd.read_csv(filename)
    length = len(df.index)  # how many names are in the data file
    list_names = []  # initialize list
    for name in range(length):  # for every index of dataframe
        list_names.append(df.iloc[name]['Full Name'])  # append full names to list of full names
    return list_names

def is_list_odd(list):
    if len(list) % 2 == 0:
        return False
    else:
        return True

def group_of_three(temp):
    dict_of_pairings[temp] = first_half_list[0] + " " + dict_of_pairings[first_half_list[0]]
    person1 = dict_of_pairings[first_half_list[0]] #need to do this before changing dict entry for first_half_list[0]
    #create string with name of temp and existing pairing, make this group of 2 the entry for person 0
    temp_string_person0 = temp + " " + dict_of_pairings[first_half_list[0]]
    dict_of_pairings[first_half_list[0]] = temp_string_person0

    temp_string_person1 = temp + " " + first_half_list[0] #found the bug
    dict_of_pairings[person1] = temp_string_person1



list_names = create_initial_list(filename)
random.shuffle(list_names) #randomize list

if is_list_odd(list_names): #can't zip two uneven parts of list, pop last var to be added later
    temp = list_names.pop()
    listWasOdd = True

first_half_list = list_names[:len(list_names)/2]
second_half_list = list_names[len(list_names)/2:]
dict_of_pairings = dict(zip(first_half_list, second_half_list))
dict_of_pairings.update(dict(zip(second_half_list, first_half_list))) #add second half

"""
take one grouping and add a third person, if there is a temp variable
1. update dict of pairings, add a value for {'third person': 'pair of people'}
    a. dict_of_pairings.update('third person') = (first_half_list(0) +dict_of_pairings(first_half_list(0))
2. update THAT pairing to reflect that there is now a third person in that group
     a. temp_string_person0 = temp + dict(first_half_list(0))
          1. dict((first_half_list(0))= temp_string_person1
    b. temp_string_person1 = temp + first_half_list(0)
        2. dict(dict(first_half_list(0)) = temp_string_person1
"""

if listWasOdd:
   group_of_three(temp)


for k in dict_of_pairings.iteritems():
    print k
