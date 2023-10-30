"""
Exercise 16.1
-----------------------------------------------------------------------------------------------------------------------------------------
Rework the lecture, and your solutions (or mine) from the Homeworks #1 through #4, to make a MyDNAStuff module.
Put as many useful nucleotide functions as possible into the module...

Rework the lecture, and your solutions (or mine) from Homework #5 to make the codon_table module with functions specified in this lecture.

Demonstrate the use of these modules to translate an amino-acid sequence in all six-frames with just a few lines of code.
The final result should look similar to Slide 10.
Your program should handle DNA sequence with N’s in it.

|--MyDNAStuff.py
|--codon_table.py
"""
# import scripts
from codon_table import *
from MyDNAStuff import *

# import sys for CLI
import sys

#file input error handling
try:
    table = read_codons_from_filename(sys.argv[1])
except:
    print("1st argument is not an ncbi codon table")
    exit(1)
try:
    seq = read_seq_from_filename(sys.argv[2])
except:
    print("2nd argument is not a sequence file")
    exit(1)

# translate sequence
for frame in (1,2,3):
    print(f'---Frame {frame}---')
    print(f'Valid Start: {is_init(table, seq[(frame-1):(frame+2)])}')
    print('Amino Acid Sequence:', translate(table,seq,frame))