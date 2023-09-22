# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 09:57:51 2023

@author: ninja
"""
"""
Modify your DNA translation program to translate in each forward frame (1,2,3)

Modify your DNA translation program to translate in each reverse (complement) translation frame too.

Modify your translation program to handle 'N' symbols in the third position of a codon
If all four codons represented correspond to the same amino-acid, then output that amino-acid.
Otherwise, output 'X'.
"""

"""
Per the taxonomy browser - the correct translation table for Bacillus anthracis
(Taxonomy ID: 1392) [https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=1392&lvl=3&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock]
is table 11 which has been downloaded into my directory as 'table_11.txt' and
uploaded to canvas as such.
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

#Defining Functions:
def translate(seq):
    """Performs basic translation using the given codon table.
    ATTN: Dependent on the above code generating the codon dictionary"""
    transcript_ini = []
    for b in range(0, len(seq), 3):
        c = seq[b:b+3]
        res = codons.get(c,"X")
        transcript_ini.append(res)
    #concatenate translated AAs
    transcript_final = "".join(transcript_ini)
    return transcript_final

#Complement will standardize non-actg bases on the "N" char
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
    #reverse list comp to compute rev_comp
    rev_comp = [complement.get(aa, "N") for aa in seq[::-1]]
    return "".join(rev_comp)



### OUTPUT

# Main Translation Loop
#translates forward and backward for each frame and outputs to terminal
for i in range(3):
    seq_framed = sequence[i:]
    protein = translate(seq_framed)
    comp_strand = translate(reverse_complement(seq_framed))
    print(f"FRAME {i+1}")
    print(f"No. of Residues: {len(protein)}")
    print(f"No. of Bases: {len(seq_framed)}")
    print(f"Given Strand: {protein}")
    print(f"Complementary Strand: {comp_strand}")


