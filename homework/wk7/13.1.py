"""
Apply the program of slide 19 to 10_Normal_Chr21.bam and find the locus with:
    - Single diploid-organism heterozygosity (approx.), and highest coverage
    - Output the locus, its alleles, and the number of high-quality reads for each allele.
    - Then, add the code to filter out bad/poor alignments (slide 20) to your program.

    Does the highest coverage heterozygous locus and its read counts change? If so, how?
"""

### command line utility
import sys

file = sys.argv[1]

### FROM SLIDE 19

import pysam
bf = pysam.Samfile(file)

# For every position in the reference
for pileup in bf.pileup('21'):
    counts = {}
    # examine every aligned read
    for pileupread in pileup.pileups:
        # get the read-base
        if not pileupread.query_position:
            continue
        readbase = pileupread.alignment.seq[pileupread.query_position]
        # count the number of each base
        if readbase not in counts:
            counts[readbase] = 0
            counts[readbase] = 0
        counts[readbase] += 1
    # if there is no variation, move on
    if len(counts) < 2:
        continue
    # otherwise, output the position, coverage and base counts
    print(pileup.pos, pileup.n, end=" ")
    for base in sorted(counts):
        print(base,counts[base], end=" ")
    print()



