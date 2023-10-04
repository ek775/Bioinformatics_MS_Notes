"""
0.  Read through and try the examples from Chapters 2-5 of BioPython's Tutorial.

1a. Download human proteins from RefSeq and compute amino-acid frequencies for the (RefSeq) human proteome.
Which amino-acid occurs the most? The least?
Hint: access RefSeq human proteins in human.protein.fasta.gz from the course data-folder.

1b. Download human proteins from SwissProt and compute amino-acid frequencies for the SwissProt human proteome.
Which amino-acid occurs the most? The least?
Hint: access SwissProt human proteins from 	http://www.uniprot.org/downloads -> “Taxonomic divisions”

1c. How similar are the human amino-acid frequencies of in RefSeq and SwissProt? 
Which amino-acids show the biggest difference in frequency?
"""

# import required packages
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from statistics import mean
import sys
import gzip

# file locations
ref_seq_human = '~/Downloads/human.protein.fasta.gz'
swiss_prot_human = '~/Downloads/uniprot_sprot_human.xml.gz'

########################################################################################################
# EXTRACT SEQUENCE DATA
########################################################################################################

def file_type(file_path):
    """evaluates a file's string to find the correct file extension and choose the appropriate biopython parser"""
    file_name = file_path.split("/")[-1]
    extensions = file_name.split(".")
    final_extension = None
    if extensions[-1]=="gz":
        final_extension = extensions[-2]
    else:
        final_extension = extensions[-1]
    # map extension name to parser argument
    matching_parser = {"fasta":"fasta", "xml":"uniprot-xml"} # add others as needed
    return matching_parser[final_extension]

# loading and parsing files - extracting sequences only to save memory
proteome_dict = {}
for i, file_path in enumerate(sys.argv[1:], start=1):
    file_name = file_path.split("/")[-1]
    extensions = file_name.split(".")
    # fasta files must be read in text mode
    mode = "r"
    if file_type(file_path)=="fasta":
        mode = "rt"
    # if compressed
    if extensions[-1]=="gz":
        # use file_type function above to identify correct parser
        # creates list of sequence strings and stores in dictionary based on files passed to program
        # added string force to resolve type errors during stats below
        proteome_dict[f"file_{i}"] = [str(record.seq) for record in SeqIO.parse(gzip.open(file_path, mode=mode), file_type(file_path))]
    # if extracted
    else:
        # same as above but using normal open instead of gzip
        proteome_dict[f"file_{i}"] = [str(record.seq) for record in SeqIO.parse(open(file_path, mode=mode), file_type(file_path))]

########################################################################################################
# AGGREGATE & COUNT AA FREQUENCIES
########################################################################################################

# concatenate AAs into single large string
frequency_dict = {}
for proteome, seq_list in proteome_dict.items():
    proteome_dict[proteome] = "".join(seq_list)
    # initialize Protein Analysis Object
    C = ProteinAnalysis(proteome_dict[proteome])
    # Calculate AA Frequency
    frequency_dict[proteome] = C.get_amino_acids_percent()

########################################################################################################
# COMPARE FREQUENCIES
########################################################################################################

# if only one file passed to the script
if len(frequency_dict)<=1:
    print("Amino Acid Frequencies in the Given Proteome:")
    print(frequency_dict["file_1"])
    print()
    # most and least common amino acid
    # list comp indexes back into dict to pull out the AA letter associated with max/min
    most_common = [i for i,m in frequency_dict["file_1"].items() if m==max(frequency_dict["file_1"].values())]
    least_common = [i for i,m in frequency_dict["file_1"].items() if m==min(frequency_dict["file_1"].values())]
    print(f"Most Common AA: {most_common[0]}")
    print(f"Least Common AA: {least_common[0]}")
    exit(0) #stop here

else:
    # initialize the final dataframe-like structure for comparison (dict x list)
    comparison_dict = {}
    for amino_acid in frequency_dict["file_1"]:
        comparison_dict[amino_acid] = []

    # append frequencies
    for proteome in frequency_dict:
        for amino_acid, freq in frequency_dict[proteome].items():
            comparison_dict[amino_acid].append(freq)
            ### Note that this approach will cause issues if an AA is found that is not in the 1st file
            ### for some reason. This is unlikely, but we're not working with actual dataframe
            ### structures at this point and without OOP there is not a very efficient way to create a 
            ### new column correctly.
    
    # calculate some descriptive stats
    stats_dict = {}
    for amino_acid, freqs in comparison_dict.items():
        # returns index of the maximum value so we know which proteome is max/min for the AA
        maximum = [(i+1,x) for i,x in enumerate(freqs) if x==max(freqs)]
        minimum = [(i+1,x) for i,x in enumerate(freqs) if x==min(freqs)]
        avg = mean(freqs)
        # store in nested dictionary
        stats_dict[amino_acid] = {"Max":maximum[0],
                                  "Min":minimum[0],
                                  "Mean":avg}
    
    # send results to terminal
    print("FREQUENCIES:")
    print(comparison_dict)
    print()
    print("DESCRIPTIVE STATISTICS:")
    print(stats_dict)
    exit(0) #stop here
