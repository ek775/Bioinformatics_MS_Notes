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

# CLI file input
try: 
    file = sys.argv[1]
    csv.DictReader(open(file))
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

def from_column(pretend_dataframe, query):
    """selects a matching column from command line argument and returns it in a dataframe-like structure"""
    selected_column = pretend_dataframe.get(query, None)
    # handles typos
    if selected_column == None:
        print("Column not found")
        exit(1)
    else:
        return {query:selected_column}

def find(query, column, pretend_dataframe):
    """finds matching items in a column of a dataframe and returns their indexes"""
    search_column = pretend_dataframe.get(column, None)
    #handle bad search column
    if search_column == None:
        print("Invalid search column")
        exit(1)
    else:
        return [i for i,item in enumerate(search_column) if item==query]

def descriptive_stats(not_a_dataframe):
    """Iterates through a dataframe-like structure and computes descriptive statistics
    for each column. Returns results in a nested dictionary similar to JSON format"""
    results = {}
    for gene in not_a_dataframe:
        data = not_a_dataframe[gene]
        results[gene] = {"MEAN": mean(data), "STD_DEV": std_dev(data)}
    return results
##################################################################
# LOAD AND PARSE DATA
##################################################################

#open file
reader = csv.DictReader(open(file))

#put data into 2D-list for access
#1D is each row, 2D is the dictionary for each
shitty_data_frame = [r for r in reader]

### collect data from each column

#initialize dict for aggregation
columns = [i for i in shitty_data_frame[1].keys()]
init_list = [[] for i in range(len(columns))]
column_aggregation = dict(zip(columns,init_list))

#unpacks each dictionary and puts values into categorized lists
for row in shitty_data_frame:
    for key in row:
        column_aggregation[key].append(Decimal(row[key]))

###################################################################
# MAIN LOOP / DESCRIPTIVE STATS
###################################################################

single_column = None
indexes = None
new_df = {}

# Accept SQL-ish arguments on CLI
for i, arg in enumerate(sys.argv):
    if arg=="FROM":
        #find column
        q = sys.argv[i+1]
        single_column = from_column(pretend_dataframe=column_aggregation, query=q)
    elif arg=="SELECT" and single_column!=None:
        # find indexes in single column
        q2 = Decimal(sys.argv[i+1])
        indexes = find(query=q2, column=q, pretend_dataframe=column_aggregation)
        # generate filtered single column dataframe
        new_df[q] = [single_column[i] for i in indexes]
    elif arg=="SELECT":
        # find indexes in whole dataframe
        q2 = Decimal(sys.argv[i+1])
        q3 = sys.argv[i+2]
        indexes = find(query=q2, column=q3, pretend_dataframe=column_aggregation)
        for i in column_aggregation:
            new_df[i] = [column_aggregation[i][x] for x in indexes]
    else:
        continue

# Compute descriptive stats
if len(new_df)==0 and single_column==None:
    print("Mean and Standard Deviation for Whole Array:")
    print(descriptive_stats(column_aggregation))
    exit(0)

if len(new_df)>0:
    print("Mean and Standard Deviation for Selected Array Data:")
    print(descriptive_stats(new_df))
    exit(0)

else:
    print(f"Mean and Standard Deviation for {single_column.keys()}")
    print(descriptive_stats(single_column))






