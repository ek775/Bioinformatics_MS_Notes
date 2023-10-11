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

### ADAPTED FROM SLIDE 19

import pysam
bf = pysam.AlignmentFile(file, "rb")

# creating data structures to persist the alignment CDF created below for analysis
refseq_snp_cdf = {}
refseq_snp_cdf_w_qc = {}

# For every position in the reference
for pileup in bf.pileup():
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
        counts[readbase] += 1
    # if there is no variation, move on
    if len(counts) < 2:
        continue
    # if SNP at this position, add this information to the nested analysis dict
    refseq_snp_cdf[f'{pileup.pos}'] = {"density":pileup.n,
                                       "bases":[(base,counts[base]) for base in sorted(counts)]
                                       }

print(dict(list(refseq_snp_cdf.items())[0:10]))

### WITH SLIDE 20

# For every position in the reference
for pileup in bf.pileup():
    counts = {}
    # examine every aligned read
    for pileupread in pileup.pileups:
        # check the read and alignment
        if pileupread.indel:
            break
        if pileupread.is_del:
            break
        al = pileupread.alignment
        if al.is_unmapped:
            break
        if al.is_secondary:
            break
        if int(al.opt("NM"))>1:
            break
        if int(al.opt("NH"))>1:
            break
        # and get the read-base
        if not pileupread.query_position:
            break
        readbase = al.seq[pileupread.query_position]
        # count the number of each base
        if readbase not in counts:
            counts[readbase] = 0
        counts[readbase] += 1
    # if there is no variation, move on
    if len(counts) < 2:
        continue
    # if SNP at this position, add this information to the nested analysis dict
    refseq_snp_cdf_w_qc[f'{pileup.pos}'] = {"density":pileup.n,
                                       "bases":[(base,counts[base]) for base in sorted(counts)]
                                       }

print(dict(list(refseq_snp_cdf_w_qc.items())[0:10]))

#documenting the nested dictionary's expected format
"""
Nested Dict Format:

refseq_snp_cdf = 
{
position(n):
    {
    "density": (number of reads aligned with position(n).)
    "bases": [(base, no. of occurences at position), etc. in descending order]
    }
}
"""

#defining results function to return the results before/after QC
def results(my_huge_dict):
    """takes my_huge_dict and gives you the location with the highest coverage"""
    result = 0 
    position = None
    for big_load in my_huge_dict:
        if my_huge_dict[big_load]["density"] >= result:
            result = my_huge_dict[big_load]["density"]
            position = big_load
            other_info = my_huge_dict[big_load]["bases"]
        else:
            continue
    return (position, result, other_info)

# print results
print("Highest Read Density Position (No QC):")
print(results(refseq_snp_cdf))
print("**************************************")
print("Highest Read Density Position (W/QC):")
print(results(refseq_snp_cdf_w_qc))