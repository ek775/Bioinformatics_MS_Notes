# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 09:56:00 2023

@author: ninja
"""

#Write a program to test whether a PCR primer is a reverse complement palindrome.
#Such a primer might fold and self-hybridize!
#Test your program on at least the following primers:
t1 = "TTGAGTAGACGCGTCTACTCAA"
t2 = "TTGAGTAGACGTCGTCTACTCAA"
t3 = "ATATATATATATATAT"
t4 = "ATCTATATATATGTAT"

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
        
        
#output from testing in ipython terminal   
"""
runcell(0, 'C:/Users/ninja/Documents/ms_bioinformatics/python_intro/homework/wk3/5.2.py')

primer_pal(t2)
Out[52]: (True, 'ttgagtagacg', 'cgtctactcaa')

primer_pal(t1)
Out[53]: (True, 'ttgagtagacg', 'cgtctactcaa')

primer_pal(t3)
Out[54]: (True, 'atatatat', 'atatatat')

primer_pal(t4)
Out[55]: False
"""
        
        
        
        
        
        