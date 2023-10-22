"""
Module is called: codon_table
Functions:
    read_codons_from_filename(filename)
        returns dictionary of codons – value is pair: (amino-acid symbol, initiation codon true/false)
    amino_acid(codon_table,codon)
        returns amino-acid symbol for codon
    is_init(codon_table,codon)
        returns true if codon is an initiation codon, false, otherwise 
    get_ambig_aa (codon_table,codon)
        Returns the single amino-acid consistent with ambiguous codon (containing N's), or X. 
    translate(codon_table,seq,frame)
        returns amino-acid sequence for DNA sequence seq
"""