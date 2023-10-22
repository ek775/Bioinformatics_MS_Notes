"""
Module is called: codon_table
Functions:
    read_codons_from_filename(filename)
        returns dictionary of codons value is pair: (amino-acid symbol, initiation codon true/false)
    amino_acid(codon_table,codon)
        returns amino-acid symbol for codon
    is_init(codon_table,codon)
        returns true if codon is an initiation codon, false, otherwise 
    get_ambig_aa (codon_table,codon)
        Returns the single amino-acid consistent with ambiguous codon (containing N's), or X. 
    translate(codon_table,seq,frame)
        returns amino-acid sequence for DNA sequence seq
"""

def read_codons_from_filename(codon_table_file):
    """Reads ncbi codon table and creates mappable dictionary"""
    f = open(codon_table_file)
    data = {}
    for l in f:
        sl = l.split()
        key = sl[0]
        value = sl[2]
        data[key] = value
    f.close()

    b1 = data['Base1']
    b2 = data['Base2']
    b3 = data['Base3']
    aa = data['AAs']
    st = data['Starts']

    translation_table = {}
    n = len(aa)
    for i in range(n):
        codon = b1[i] + b2[i] + b3[i]
        translation_table[codon] = (aa[i], st[i])
    
    return translation_table

def amino_acid(translation_table, codon):
    """translates a given codon according to a given codon table"""
    residue = translation_table[codon][0]
    return residue

def is_init(translation_table, codon):
    """reads codon table (start, stop, neutral) value and returns True/False if given codon is/is not a start codon"""
    start = translation_table[codon][1]
    t = False
    if start == "M":
        t = True
    else:
        t = False
    return t

def get_ambig_AA(translation_table, given_codon):
    """adjunct for the translate function handling partial matches in the codon table"""
    residue = None
    #find partial match entries in codon table
    #note that this only checks 3rd base mismatches - this is based on accepted theory of loose 3rd base pairing
    partial_match = [cdn for cdn in translation_table.keys() if cdn[0:1]==given_codon[0:1]]
    partial_match_values = [translation_table[r] for r in partial_match] #find relevant translations
    if len(set(partial_match_values))==1:
        residue = partial_match_values[0][0]
    #if unable to resolve partial match, return "X"
    else:
        residue = "X"
    return residue

def translate(translation_table, seq, frame=1):
    """translates a given sequence based on the given translation table, within a specified translation frame.
    frame defaults to 1 if not specified."""
    #correct frame value if bad range
    if frame not in range(1,4):
        frame = (frame + 1)%3
    frame += (-1)
    # translate
    peptide = []
    transcript = seq[frame:] # slice according to translation frame
    for i in range(0, len(seq), 3):
        codon = transcript[i:i+3]
        if len(transcript) < 3:
            continue
        else:
            residue = translation_table.get(codon, get_ambig_AA(translation_table, codon))
            peptide.append(residue[0])
    return ''.join(peptide)