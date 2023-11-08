#import classes from 19.1.py
from objects import *
# import sys for CLI
import sys

#file input error handling
try:
    table = read_codons_from_filename(sys.argv[1])
except:
    print("1st argument must be an ncbi codon table")
    exit(1)
try:
    seq = read_seq_from_filename(sys.argv[2])
except:
    print("2nd argument must be a sequence file")
    exit(1)

# translate sequence
for frame in (1,2,3):
    print(f'---Frame {frame}---')
    print(f'Valid Start: {is_init(table, seq[(frame-1):(frame+2)])}')
    print('Amino Acid Sequence:', translate(table,seq,frame))