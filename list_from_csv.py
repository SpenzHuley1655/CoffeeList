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


list_names = create_initial_list(filename)
random.shuffle(list_names) #randomize list

if is_list_odd(list_names):
    temp = list_names.pop()
first_half_list = list_names[:len(list_names)/2]
second_half_list = list_names[len(list_names)/2:]

dict_of_pairings = dict(zip(first_half_list, second_half_list))
print dict_of_pairings