# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 10:26:54 2023

@author: ninja

Exercise 11.1:
    
Write a program that reads the microarray data in “data.csv” 
and computes the mean and standard deviation of the expression 
values of a specific gene overall, and within each sample category.

"""

# loading packages
import csv
#import sys

#try: 
    #file = sys.argv[1]
#except: 
    #print("Missing File Argument")
    #exit(1)

##################################################################
# DEFINING MATHEMATICAL FUNCTIONS
##################################################################

def mean():
    pass

def average():
    pass

##################################################################
# LOAD AND PARSE DATA
##################################################################

file = 'data.csv'
reader = csv.DictReader(open(file))

#put data into 2D-list for access
#1D is each row, 2D is the dictionary for each
shitty_data_frame = [r for r in reader]
#print(shitty_data_frame)

### collect data from each column

#initialize dict for aggregation
columns = [i for i in shitty_data_frame[1].keys()]
init_list = [[] for i in range(len(columns))]
column_aggregation = dict(zip(columns,init_list))
#print(column_aggregation)

#aggregate data
#unpacks each dictionary and puts values into categorized lists
for row in shitty_data_frame:
    for key in row:
        column_aggregation[key].append(row[key])

#print(column_aggregation)

### convert string values to numerical data type









