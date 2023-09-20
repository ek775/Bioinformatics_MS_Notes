# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:28:02 2023

@author: ninja
"""

#4.1
#Write a Python program to compute the reverse complement of a codon
#Use my solution to Homework #1 Exercise #1 as a starting point
#Add the “complement” function of this lecture
#(slide 9) as provided.
#Modularize! Place the reverse complement code in a new function. 
#Call the new function with a variety of codons
#Change the complement function to handle upper and lower-case nucleotide symbols.
#Test your code with upper and lower-case codons.



###Complement Fx
def complement(init_strand):
    """
    generates the complementary base pair sequence
    for a given strand of DNA

    Parameters
    ----------
    init_strand : str
        given strand of DNA

    Returns
    -------
    complementary sequence

    """
    #handle case
    init_strand = init_strand.upper()
    
    #main loop with conditionals
    complement = ""
    for b in init_strand:
        if b=="A":
            complement += "T"
        if b=="T":
            complement += "A"
        if b=="C":
            complement += "G"
        if b=="G":
            complement += "C"
    
    return complement



###Reverse Fx
def reverse(starting_sequence):
    """
    Takes a sequence of DNA and returns the reverse 
    of the bases.

    Parameters
    ----------
    starting_sequence : str
        sequence of DNA to be reversed

    Returns
    -------
    reversed DNA sequence

    """
    #handling letter case
    starting_sequence = starting_sequence.upper()
    
    #main loop, appends in reverse order
    new_seq = ""
    for i in range(1, len(starting_sequence)+1):
        new_seq += starting_sequence[-i]
        
    return new_seq
    
#Reverse-Complement Fx
def reverse_complement(seq):
    """
    returns the reverse complement of a DNA strand

    Parameters
    ----------
    seq : str
        given DNA strand

    Returns
    -------
    seq_c : str
        reverse complementary strand

    """
    seq_b = reverse(seq)
    seq_c = complement(seq_b)
    return seq_c
    
    
    
    
    
    
    
    
    
    
    