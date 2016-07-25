import csv
import pandas as pd
import random

df = []
filename = 'Employees_Birthday_Report_FINAL.csv'
df2 = []
filename2 = 'Global_Pairs.csv'

def create_initial_list(filename, df):
    """
    Inputs a .csv filename
    returns a list of full names from the file
    """
    df = pd.read_csv(filename)
    length = len(df.index)  # how many names are in the data file
    list_names = []  # initialize list"no
    for name in range(length):  # for every index of dataframe
        list_names.append(df.iloc[name]['Full Name'])  # append full names to list of full names
    return list_names

def create_global_pairs_list(filename, df):
    """
    Returns a list of all previous coffee pairings
    References the Global_Pairs.csv file
    """
    df = pd.read_csv(filename)
    length = len(df.index)
    list_global_pairs = []
    for name in range(length):
        list_global_pairs.append(df.iloc[name]['Name 1'])
        list_global_pairs.append(df.iloc[name]['Name 2'])
    return list_global_pairs

def make_dict_global_pairs():
    dict_global_pairs = dict()
    for name in range(0, len(list_global_pairs), 2):
        value1 = list_global_pairs[name]
        value2 = list_global_pairs[name+1]
        dict_global_pairs[value1] = value2
        dict_global_pairs[value2] = value1
    return dict_global_pairs

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



Valid_Pairing = False
while not(Valid_Pairing):

    list_names = create_initial_list(filename, df)
    random.shuffle(list_names) #randomize list

    list_global_pairs = create_global_pairs_list(filename2, df2)
    dict_global_pairs = make_dict_global_pairs()

    if is_list_odd(list_names): #can't zip two uneven parts of list, pop last var to be added later
        temp = list_names.pop()
        listWasOdd = True

    first_half_list = list_names[:len(list_names)/2]
    second_half_list = list_names[len(list_names)/2:]
    dict_of_pairings = dict(zip(first_half_list, second_half_list))
    dict_of_pairings.update(dict(zip(second_half_list, first_half_list))) #add second half


    if listWasOdd:
       group_of_three(temp)

    match = False
    for j in dict_of_pairings.iteritems():
        for k in dict_global_pairs.iteritems():
             if j == k:
                 match = True

    if match == False:
        Valid_Pairing = True

with open('Global_Pairs.csv', 'ab') as f: #NEED TO MAKE IT APPEND AND ALSO NOT CREATE SPACES BETWEEN ROWS
    w = csv.writer(f)
    w.writerows(dict_of_pairings.items())


# list_name_length = len(list_names)
# df2 = pd.read_csv('Global_Pairs.csv')
# for name in list_names:
#     df2.loc[name]['Name 1'] = name
#     df2.loc[name]['Name 2'] = dict_of_pairings[name]