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
from decimal import *
import sys

# CLI functionality
try: 
    file = sys.argv[1]
except: 
    print("Missing File Argument")
    exit(1)

##################################################################
# DEFINING MATHEMATICAL FUNCTIONS
##################################################################

def mean(data):
    """Accepts list-like column of numerical values and returns the mean"""
    return sum(data)/len(data)

def std_dev(data):
    """Accepts list-like column of numerical values and returns the 
    standard deviation"""
    avg = mean(data)
    numerator = sum([(i-avg)**2 for i in data])
    denominator = len(data)-1
    return (numerator/denominator)**Decimal(0.5)

##################################################################
# LOAD AND PARSE DATA
##################################################################

#file = 'data.csv'
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

#unpacks each dictionary and puts values into categorized lists
for row in shitty_data_frame:
    for key in row:
        column_aggregation[key].append(Decimal(row[key]))

#print(column_aggregation)

###################################################################
# COMPUTE DESCRIPTIVE STATS
###################################################################

#main loop iterates through aggregated data columns
#creates nested dict object with organized results
results = {}
for gene in column_aggregation:
    data = column_aggregation[gene]
    results[gene] = {"MEAN": mean(data), "STD_DEV": std_dev(data)}

#send results to terminal 
print(results)
exit(0)






