# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 00:12:00 2023

@author: ninja
"""

"""
Write a program that takes a codon table file (such as standard.code from the 
lecture) and a file containing nucleotide sequence (anthrax_sasp.nuc) as 
command-line arguments, and outputs the amino-acid sequence.

Modify your program to indicate whether or not the initial codon is consistent 
with the codon table's start codons.

Use NCBI's taxonomy resource to look up and download the correct codon table 
for the anthrax bacterium. Re-run your program using the correct codon table. 
Is the initial codon of the anthrax SASP gene a valid translation start site?

"""

#import sys utility
import sys

#command line arguments
seq_file = sys.argv[1]
table = sys.argv[2]



### SEQUENCE FILE PARSING

file = open(seq_file)
sequence = "".join(file.read().split())
file.close()



### TABLE FILE PARSING (modified from lecture)

#explicit standard.code arg replaced with CLI argument
#changed structure of init dict to map codons to given value in ncbi codon table

f = open(table)
data = {}
for l in f:
    sl = l.split()
    key = sl[0]
    value = sl[2]
    data[key] = value
f.close()

b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
aa = data['AAs']
st = data['Starts']

codons = {}
init = {}
n = len(aa)
for i in range(n):
    codon = b1[i] + b2[i] + b3[i]
    codons[codon] = aa[i]
    init[codon] = st[i]

#codons k,v = codon,AA
#init k,v = codon,(start,stop,neutral)



### TRANSLATE AA SEQUENCE

transcript_ini = []

#main translation loop
for b in range(0, len(sequence), 3):
    c = sequence[b:b+3]
    res = codons[c]
    transcript_ini.append(res)
    
#concatenate final transription
transcript_final = "".join(transcript_ini)



### TEST FOR VALID START

#assumes first codon not valid
valid_init = False

#init key for first codon should equal value "M"
if init[sequence[0:3]] == "M":
    valid_init = True
else:
    pass



### OUTPUT
"""
Per the taxonomy browser - the correct translation table for Bacillus anthracis
(Taxonomy ID: 1392) [https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=1392&lvl=3&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock]
is table 11 which has been downloaded into my directory as 'table_11.txt' and
uploaded to canvas as such.

According to both tables, TTG is a valid start codon, thus, the code below
should print 'true' for either codon table.
"""
#state whether start codon is valid
print(f"First codon is valid start: {valid_init}")
#return sequence
print(transcript_final)



























