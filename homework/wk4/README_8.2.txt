METHODS
#####################################################################################

The program has 4 key components: Sequence File Parsing, Table File Parsing, Computational Translation, and Start Codon Validation. Table File Parsing and translation into python dictionaries was accomplished using code from lecture modified to accept a command line argument for the given file and to restructure the "init" dictionary values as one of the original ncbi "M", "-", or "*" characters. More specific details of changes can be found in the code file.

Validation of the start codon is accomplished by mapping the given sequence to its given start/stop/neutral value in the given ncbi translation table, and was easily accessed after some small changes in the file parsing step. 

*****
I have uploaded the appropriate codon table from ncbi in the same format as the given codon table as "table_11.txt" for ease of reproducability. According to the taxonomy browser at ncbi, this is the appropriate table for Bacillus anthracis. 

Bacillus anthracis (Taxonomy ID = 1392):

https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=1392&lvl=3&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock
*****

DISCUSSION
#####################################################################################

This exercise is a very straightforward mapping exercise that utilizes dictionaries to simulate the translation of sequences into their Amino Acid counterparts. The most difficult step in this exercise is actually not the given task, but rather the parsing and conversion of ncbi codon tables into useful dictionaries/hash tables that can efficiently compute the theoretical amino acid translation of DNA sequences. All of the code for doing this in the given formats was given to us in lecture, however, so a few minor modifications are all that was necessary. 

Given this issue with file formats and parsing issues, it is worth noting that having standardized file formats and parsers would go a long way towards accelerating bioinformatics research and the development of research tools. 
