# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:34:45 2023

@author: ninja
"""

"""
6.1) Extend your solution for Exercise 1 from Lecture 5 to get its two PCR primers from the command-line.

6.2) Write a command-line program for manipulating a DNA sequence:
DNA sequence in a file, with the filename provided on the command-line
Manipulation command also provided on the command-line:
Command is one of: Complement, Reverse, or ReverseComplement
Print the DNA sequence, and the appropriate manipulation of the DNA sequence to the terminal.
"""

### copied necessary functions to this script from 5.2.py


def reverse_complement(seq):
    """takes in sequence of length n and returns the reverse complement"""
    #handle case
    seq = seq.lower()
    rev_comp = ""
    #reverse the sequence
    for i in range(1, len(seq)+1):
        base = seq[-i]
        origin = "atcg"
        complement = "tagc"
        #compute complement
        if base in origin:
            o = origin.find(base)
            c = complement[o]
            rev_comp += c
        #non-valid or unknown bases = x
        else:
            rev_comp += "x"
    return rev_comp


def primer_pal(primer):
    """determines if a given dna string is a palindrome. Returns True/False along with associated palindrome if true."""
    #handle case
    primer = primer.lower()
    #if primer has odd number of bases, remove middle base
    if len(primer)%2 != 0:
        extra_base_loc = int(len(primer)//2)
        front = primer[:extra_base_loc]
        back = primer[extra_base_loc+1:]
        primer = front + back
        
    #split primer in half
    front_half = primer[:int(len(primer)/2)]
    back_half = primer[int(len(primer)/2):]
    #generate reverse complement seq
    test_seq = reverse_complement(front_half)
        
    #test for palindrome
    if test_seq == back_half:
        return True, front_half, back_half
    else:
        return False




### MAIN
"""Allows user to interact with this script file from a standard terminal by 
calling the script, a function name, and a sequence or text file.

example format: 
    python 6.1.py {palindrome, rev_comp} {sequence_as_string, sequence_file.txt}
   
*Note that this should be run from the base machine terminal, not an 
interactive python terminal.
"""

#import sys module
import sys

#accept command line arguments (1) function to execute, (2) sequence file (txt)
func_arg = sys.argv[1]
seq_arg = sys.argv[2]


##load sequence as string literal or text file


#empty string for concatenation
input_seq = ""
#attempt to read from file first
try:
    #open file, read contents, and remove whitespace
    input_seq = input_seq.join(open(seq_arg).read().split())
#if not a file, likely a sequence - will fail here if none of the above
except:
    input_seq += seq_arg


##processing requested output


#map function call
valid_fx = {"palindrome": primer_pal(input_seq),
            "rev_comp": reverse_complement(input_seq)}

#validate
if func_arg not in valid_fx:
    print("invalid function")
    
#call the function and print the desired output    
else:
    print(valid_fx[func_arg])





### OUTPUT from TESTING in gitbash terminal:
#NOTE: function validation working properly in line 2

#palindrome fx testing
"""    
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$ python 6.1.py palindrome TEN1_forward_primer.txt
False
(BINF)
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$ python 6.1.py palindrom TEN1_forward_primer.txt
invalid function
(BINF)
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$
"""

#rev_comp fx testing
"""
(BINF)
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$ python 6.1.py rev_comp TEN1_reverse_primer.txt
acatttggcaggttgtgcct
"""

#with optional string input
"""
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$ python 6.1.py rev_comp "AAAAAAAAATTT"
aaattttttttt
(BINF)
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$ python 6.1.py rev_comp AAAAAAAAATTT
aaattttttttt
(BINF)
ninja@DESKTOP-01SKGG9 MINGW64 ~/Documents/ms_bioinformatics/python_intro/homework/wk3
$ python 6.1.py rev_comp TEN1_reverse_primer.txt
acatttggcaggttgtgcct
"""
































