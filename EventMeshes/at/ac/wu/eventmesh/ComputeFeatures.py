'''
Created on Jan 19, 2018

@author: Saimir Bala <saimir.bala@gmail.com>
'''

import pandas as pd
from numpy import loadtxt


import csv

eventlog = 'allEvents.csv'

csvfile = open(eventlog, 'r')
reader = csv.DictReader(csvfile)
dict_list = []

for line in reader:
    dict_list.append(line)

# print dict_list

df = pd.DataFrame(dict_list)



# df = pd.read_csv(eventlog, error_bad_lines=False)

