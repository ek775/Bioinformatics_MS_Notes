#Write a program using NCBI's E-Utilities to find the ids of RefSeq human BRCA2 proteins from NCBI (esearch)
#Extend your program to write out a FASTA file of the protein sequences of these entries (efetch)

"""Upload the FASTA file to NCBI’s interactive Blast website, and search for (potential) mouse orthologs
Use the protein vs protein search (blastp)
Use refseq_protein as the search database
Set the organism field to “Mus musculus”
Which mouse protein is most similar to its human counterpart?
"""

#import packages
from Bio import Entrez
from Bio import SeqIO

#variables
Entrez.email = 'ek990@georgetown.edu'

#search for BRCA2 variants
handle = Entrez.esearch(db='protein', term="Homo sapiens[Organism] AND BRCA2[Gene Name] AND REFSEQ")
result = Entrez.read(handle)
handle.close()

#read results
idlist = ','.join(result["IdList"])
handle = Entrez.efetch(db="protein", id=idlist, rettype='gb')
records = list(SeqIO.parse(handle, "genbank"))
#send to file
with open("BRCA2.gb", "w") as handle_out:
    SeqIO.write(records, handle_out, "gb")
#convert to fasta
SeqIO.convert("BRCA2.gb", "genbank", "BRCA2.fasta", "fasta")

# Best Blast Mouse Ortholog:
# Accession Num = NP_001074470.1
# URL = https://www.ncbi.nlm.nih.gov/protein/NP_001074470.1?report=genbank&log$=prottop&blast_rank=1&RID=MNU3TYHE013