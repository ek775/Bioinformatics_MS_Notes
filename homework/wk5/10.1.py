# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:40:00 2023

@author: ninja
"""
"""
Write a reverse complement function (and package it up as a program) as compactly as possible (1-2 lines), using the techniques introduced today.
Hint: Use a dictionary for complement, reversed on the sequence, list comprehension to apply the get method of the dictionary, and the join method for strings. 
"""

def reverse_complement(seq):
    """Computes reverse complement strand"""
    complement = {"A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C",
                  "a":"t",
                  "t":"a",
                  "c":"g",
                  "g":"c"}
    #I have broken out the concatenation and list-comp steps for clarity,
    #however, the list-comp can be wrapped in the str.join() call below 
    #for a one line solution.
    rev_comp = [complement.get(aa, "N") for aa in seq[::-1]]
    return "".join(rev_comp)