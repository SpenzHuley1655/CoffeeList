import pandas as pd
import random
import csv

filename = 'Employees_Birthday_Report_FINAL.csv'
outputfilename = 'mycsvfile.csv'
def create_initial_list(filename):
    """
    Inputs a .csv filename
    returns a list of full names from the file
    """
    df = pd.read_csv(filename)
    length = len(df.index)  # how many names are in the data file
    index = df.index
    list_names = []  # initialize list
    for name in range(length):  # for every index of dataframe
        list_names.append(df.iloc[name]['Full Name'])  # append full names to list of full names
    return list_names

def is_list_odd(list):

    if len(list) % 2 == 0:#if even
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
random.shuffle(list_names)#randomize list

if is_list_odd(list_names): #can't zip two uneven parts of list, pop last var to be added later
    temp = list_names.pop()
    listWasOdd = True

first_half_list = list_names[:len(list_names)/2]
second_half_list = list_names[len(list_names)/2:]
dict_of_pairings = dict(zip(first_half_list, second_half_list))
dict_of_pairings.update(dict(zip(second_half_list, first_half_list)))#add second half


if listWasOdd:
   group_of_three(temp)

def write_to_csv(outputfilename):
    with open('mycsvfile.csv','a') as f: #write pairs to a row
        w = csv.writer(f)
        w.writerows(dict_of_pairings.items())

