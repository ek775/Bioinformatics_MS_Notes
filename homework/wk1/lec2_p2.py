#variables
codon = "ATG"
dna = "gcatcacgttatgtcgactctgtgtggcgtctgctggg"

#Write a python program to find the position and the translation frame (1, 2, or 3) of the first start-codon in the DNA sequence:
"""uses .find() method to locate first start codon, then returns the translation frame and start position relative to the whole sequence"""

start_position = dna.find("atg") + 1
translation_frame = (start_position % 3)

print("first start codon:", start_position)
print("translation frame position:", translation_frame)
