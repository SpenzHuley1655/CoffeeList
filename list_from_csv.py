import pandas as pd
import random
import csv

FILENAME = 'Employees_Birthday_Report_FINAL.csv'
OUTPUTFILENAME = 'mycsvfile.csv'

def main():
    init_list = create_initial_list(FILENAME)
    if is_list_odd(init_list):
        temp = pop_name(init_list)
        unfinished_dict = create_dict(init_list)
        finished_dict = group_of_three(temp, unfinished_dict, init_list)
    else:
        finished_dict = create_dict(init_list)
    write_to_csv(OUTPUTFILENAME, finished_dict)
    return

# Str -> list
# Create a list-of names from a string indicating a filename
def create_initial_list(filename):
    df = pd.read_csv(filename)
    length = len(df.index)  # how many names are in the data file
    list_names = []  # initialize list
    for name in range(length):  # for every index of dataframe
        list_names.append(df.iloc[name]['Full Name'])  # append full names to list of full names
    return list_names

# List -> Boolean
# Check if the given list is odd
def is_list_odd(list):
    return (len(list) % 2 == 1)

# list -> String
# Temporarily remove a string from the list-of strings
def pop_name(list_names): #can't zip two uneven parts of list, pop last var to be added later
    temp = list_names.pop()
    return temp

# [List-of Names] -> Dict
# Create a dict from a given list of names, pairing people randomly
def create_dict(alon):
    random.shuffle(alon)#randomize list
    first_half_list = alon[:len(alon)/2]
    second_half_list = alon[len(alon)/2:]
    dict_of_pairings = dict(zip(first_half_list, second_half_list))
    dict_of_pairings.update(dict(zip(second_half_list, first_half_list)))#add second half
    return dict_of_pairings

# String Dict [List-of Names] -> Dict
# Take the "odd man out" and pair them with 2 other people
def group_of_three(temp, dict_of_pairings, alon):
    first_half_list = alon[:len(alon) / 2]
    dict_of_pairings[temp] = first_half_list[0] + " " + dict_of_pairings[first_half_list[0]]
    person1 = dict_of_pairings[first_half_list[0]]
    temp_string_person0 = temp + " " + dict_of_pairings[first_half_list[0]]
    dict_of_pairings[first_half_list[0]] = temp_string_person0
    temp_string_person1 = temp + " " + first_half_list[0]
    dict_of_pairings[person1] = temp_string_person1
    return dict_of_pairings

def write_to_csv(outputfilename, aDict):
    with open(outputfilename,'wb') as f: #write pairs to a row
        w = csv.writer(f)
        w.writerows(aDict.items())

if __name__ == '__main__':
    main()
