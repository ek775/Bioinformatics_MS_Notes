# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 14:10:45 2023

@author: ninja
"""
"""
5.1) Use PrimerBank (“google PrimerBank”) to look up PCR primers for your favorite gene
Use Search By: “NCBI Gene Symbol”, Species: “Human” to find PCR primers for your gene. 
Write a program to compute the reverse complement sequence of both the forward and reverse primer (in one program).


Chosen gene: Telomerase
Harvard/MGH URL: https://pga.mgh.harvard.edu/cgi-bin/primerbank/new_search2.cgi

Gene Descriptions:
NCBI GeneID	100134934
GenBank Accession	NM_001113324
NCBI Protein Accession	NP_001106795
Species	Human
Coding DNA Length	372
Gene Description	Homo sapiens TEN1 telomerase capping complex subunit homolog (S. cerevisiae) (TEN1), mRNA.

Primer Pair 1 (Click here for cDNA and amplicon sequence):
PrimerBank ID	319918877c1
Amplicon Size	92
Sequence (5' -> 3')	Length	Tm	Location
Forward Primer	CCCAAACCTGGGACCTATTACC	22	61.8	10-31
Reverse Primer	AGGCACAACCTGCCAAATGT	20	62.6	101-82
"""

#primers
forward_primer = "CCCAAACCTGGGACCTATTACC"
reverse_primer = "AGGCACAACCTGCCAAATGT"

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


#testing with telomerase subunit primers
test_primers = [forward_primer, reverse_primer]

for primer in test_primers:
    print(f"Original: {primer}, \n Reverse-Complement: {reverse_complement(primer)}")
    
    
#my terminal output:
"""
In [2]: runcell(0, 'C:/Users/ninja/Documents/ms_bioinformatics/python_intro/homework/wk3/5.1.py')
Original: CCCAAACCTGGGACCTATTACC, 
 Reverse-Complement: ggtaataggtcccaggtttggg
Original: AGGCACAACCTGCCAAATGT, 
 Reverse-Complement: acatttggcaggttgtgcct
"""
















