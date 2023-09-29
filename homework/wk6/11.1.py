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
import sys

#try: 
    #file = sys.argv[1]
#except: 
    #print("Missing File Argument")
    #exit(1)

file = "~/Documents/ms_bioinformatics/python_intro/homework/wk6/data.csv"

reader = csv.DictReader(open(file))








