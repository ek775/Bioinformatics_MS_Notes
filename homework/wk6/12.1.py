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
import Bio.SeqIO as bio
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
    matching_parser = {"fasta":"fasta"
                       "xml":"uniprot-xml"} # add others as needed
    return matching_parser[final_extension]

# load and parse files
proteome_dict = {}
for i, file_path in enumerate(sys.argv):
    file_name = file_path.split("/")[-1]
    extensions = file_name.split(".")
    # if compressed
    if extensions[-1]=="gz":
        proteome_dict[f"file_{i}":[record.seq for record in "parser.gz"]]
    # if uncompressed
    else:
        proteome_dict[f"file_{i}":[record.seq for record in "parser"]]

# extract sequences and store in list

########################################################################################################
# AGGREGATE & COUNT AA FREQUENCIES
########################################################################################################



########################################################################################################
# COMPARE FREQUENCIES
########################################################################################################


