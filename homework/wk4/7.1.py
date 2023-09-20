# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:49:08 2023

@author: ninja
"""
#Exercise 7.1
######################################################################
# Write a command-line program for computing the reverse complement of primer pairs:
# Primer pairs are listed in a file, one per line.
# Forward and reverse primers on each line are separated by a space. Ignore anything after the first two space separated “words” on each line.
# e.g. Example input file: here
# Print the reverse complement of each primer of the pair in the same format as the input file. 
# Hint: Use open(…).read() to read the entire contents of the file into a string…



# Main
#######################################################################

#import sys for command line utility
import sys
#store file name
file = sys.argv[1]

#read file contents
raw = "".join(open(file).read())

#remove comments
primers = []
for line in raw.splitlines():
    for string in line.split():
        if "#" in string:
            break
        else:
            primers.append(string)
            
#print(primers)    

#primers should now be extracted in a list and stored in primers

### define critical functions
def complement(strand):
    """takes in a dna sequence and returns the complement"""
    strand_comp = ""
    origin = "ATCGatcg"
    comp = "TAGCtagc"
    for i in strand:
        if i in origin:
            x = origin.find(i)
            c = comp[x]
            strand_comp += c
        else:
            strand_comp += "x"
    return strand_comp

def reverse(sequence):
    """reverses a given string"""
    rev = ""
    for i in range(1, len(sequence)+1):
        rev += sequence[-i]
    return rev

def reverse_complement(seq):
    """computes reverse complement of a dna sequence"""
    return reverse(complement(seq))


### iteratively compute reverse complement for primers in given file

#generate new list of reverse complement primers
rev_comp_primers = [reverse_complement(p) for p in primers]

#formatting output
print("Here are your requested primers and their reverse complements:")
for x in range(len(primers)):
    print(f"Original: {primers[x]} | Final: {rev_comp_primers[x]}")




