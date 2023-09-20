# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:11:42 2023

@author: ninja
"""

"""
Using just the concepts introduced so far, find as many (different!) ways as 
possible to code DNA reverse complement (at least 3!)
"""

##### OLD RELIABLE (see exercise 7.1)
#exceptionally literal

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



##### METHOD 2
#use dict for complement conversion
#fundamental approach is same

def complement_2(strand):
    """maps dna sequence to complement via dict"""
    strand_comp = ""
    comp_dict = {
        "A":"T",
        "T":"A",
        "C":"G",
        "G":"C",
        "a":"t",
        "t":"a",
        "c":"g",
        "g":"c"
        }
    #main loop
    for i in strand:
        if i in comp_dict:
            c = comp_dict[i]
            strand_comp += c
        else:
            strand_comp += "x"
    return strand_comp

def reverse_complement_2(seq):
    """computes reverse complement of a dna sequence"""
    #no change to reverse fx in this iteration
    return reverse(complement_2(seq))



##### METHOD 3
#uses built in map() and reversed functions() with list comp (and lambda for brevity)
#note there are still effectively 2 main loops in this scheme
#potentially memory intensive due to list comps
#also no handling of typos / unknown bases in sequence

#potentially significant speed advantage based on testing below
#this is copied/pasted from ipython my ipython terminal - recommend verifying on your machine
"""
reverse_complement_3(sequence)
Out[16]: 'TCGATGCACAATGGCTAAGCTTACGTTTTTTTTTTTTTTTTTTTTTT'

%timeit reverse_complement(sequence)
16.8 µs ± 1.5 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%timeit reverse_complement_3(sequence)
6.26 µs ± 286 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)

long_seq = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCGCTAGCTAGCTAGCTAGCGTACAGCATCGACTAGCTACGATCGATCGACTAGCATCACTTAGCTAGCTAGCTAGCTAGCTACGATCGATCGATCGACTCGACAGCTAGCTACGTACGACTC"

%timeit reverse_complement_3(long_seq)
54 µs ± 222 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%timeit reverse_complement_2(long_seq)
110 µs ± 12.9 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

%timeit reverse_complement(long_seq)
160 µs ± 11 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
"""

def reverse_complement_3(seq):
    """maps bases to their complement and reverses their order with built-in
    functions/iterators to find the reverse_complement sequence. Returns a string."""
    
    comp_dict = {
    "A":"T",
    "T":"A",
    "C":"G",
    "G":"C",
    "a":"t",
    "t":"a",
    "c":"g",
    "g":"c"
    }
    
    #list comp to generate complementary bases with map()
    #seq passed as iterable to lambda which converts each base via dict
    comp = [b for b in map(lambda x: comp_dict[x], seq)]
    #list comp to generate reversal with reversed()
    rev_comp = [b for b in reversed(comp)]
    #concatenate list
    rev_comp = "".join(rev_comp)
    #results
    return rev_comp
    


##### METHOD 4
#utilize the enumerate function, dictionary conversion from method 2

def reverse_4(sequence):
    """reverses a given string"""
    rev = ""
    for i, base in enumerate(sequence, start=1):
        rev += sequence[-i]
    return rev

def reverse_complement_4(seq):
    """computes reverse complement of a dna sequence"""
    return reverse_4(complement_2(seq))

#output from fx testing
"""
reverse_complement_4(sequence)
Out[24]: 'TCGATGCACAATGGCTAAGCTTACGTTTTTTTTTTTTTTTTTTTTTT'

%timeit reverse_complement_4(sequence)
10.3 µs ± 335 ns per loop (mean ± std. dev. of 7 runs, 100,000 loops each)
"""






















