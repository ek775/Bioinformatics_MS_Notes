# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:45:31 2023

@author: ninja
"""
"""
Write a program to compute and output the frequency of each nucleotide in a DNA sequence using a dictionary (see lec. 9).
Output the frequencies in most-occurrences to least-occurrences order.
"""
# CLI Functionality
import sys

seq_file = sys.argv[1]

### SEQUENCE FILE PARSING
file = open(f"./{seq_file}", "r")
strange_women = "".join(file.read().split())
file.close()

### COUNTING
swords_in_pond = len(strange_women)
pond = {}
for sword in strange_women:
    if sword in pond:
        pond[sword] += 1
    else:
        pond[sword] = 1
  
### DISTRIBUTING SWORDS (calculating frequency)
shrubbery = {}
for sword in pond:
    shrubbery[sword] = pond[sword]/swords_in_pond

### OUTPUT
for i in shrubbery:
    print(f"{i}:\t{shrubbery[i]}")


#shits n giggles
print()
print("Strange women lying in ponds distributing swords is no basis for a system of government!")