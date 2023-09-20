#variables
codon = "ATG"
dna = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

#Write a python program to print out the codon for Methionine (aka the start codon) backwards in lower-case symbols.
"""Concatenates each string indice in reverse order (explicitly). Outputs the resulting string in the desired format to the terminal via a print statement"""

reverse = codon[-1] + codon[-2] + codon[-3]
print(reverse.lower())