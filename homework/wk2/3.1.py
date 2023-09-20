# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:25:44 2023

@author: ninja
"""

#Problemset 3.1

#input data
anthrax_sasp = "TTGAGTAGACGAAGAGGTGTCATGTCAAATCAATTTAAAGAAGAGCTTGCAAAAGAGCTAGGCTTTTATGATGTTGTTCAGAAAGAAGGATGGGGCGGAATTCGTGCGAAAGATGCTGGTAACATGGTGAAACGTGCTATAGAAATTGCAGAACAGCAATTAATGAAACAAAACCAGTAG"

#variables
methionine_codon = "ATG"


#starts with methionine codon?
if anthrax_sasp[0:2]==methionine_codon:
    print("SASP gene starts with methionine")
else:
    print("SASP gene does not start with methionine")


#does sasp gene have a frame 1 Met codon?
#locate Met codon
met_loc = anthrax_sasp.find(methionine_codon)+1
#determine translation frame location
met_frame = met_loc%3
#return frame location to terminal
print(f'SASP gene Methionine starts in frame position {met_frame}')


#How many nucleotides in the SASP gene?
print(f'SASP gene is {len(anthrax_sasp)} bases in length')


#How many amino-acids in the SASP protein?
print(f'There are {len(anthrax_sasp)//3} residues coded in the SASP gene')

def start_loc(seq):
    seq.upper()
    loc = seq.find("ATG")
    return loc
def stop_loc(gene):
    gene = gene.upper()
    exon = ""
    for p in range(start_loc(gene), len(gene), 3):
        acid = gene[p:p+3]
        if acid == "TAA":
            break
        if acid == "TAG":
            break
        if acid == "TGA":
            break
        else:
            exon += acid
    return exon        
def residue_count(sequence):
    protein_len = len(stop_loc(sequence))//3
    return protein_len

print(f"There are {residue_count(anthrax_sasp)} residues in the SASP protein")

#What is the GC content (% G or C nucleotides) of the SASP gene?

#begin by defining a count function (because documentation isn't a thing yet...)
def count(token, document):
    """
    Iterates through a string and counts the number of times a given query string occurs within.

    Parameters
    ----------
    token : str
        target query.
    document : str
        body of text to be searched.

    Returns
    -------
    number of times token occurs in given document as an integer value

    """
    #count variable
    count = 0
    #main loop
    for i in document:
        if i==token:
            count += 1
        else:
            continue
    #output
    return count

#count g, count c, then determine %
no_g = count("G", anthrax_sasp)
no_c = count("C", anthrax_sasp)

gc_percent = ((no_g + no_c)/len(anthrax_sasp))*100
#print percent to terminal
print(f"SASP gene has {gc_percent}% GC richness")