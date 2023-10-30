# basic sequence manipulation fx

def read_seq_from_filename(seq_filename):
    """reads a line-based file containing a dna sequence"""
    seq_file = open(seq_filename)
    dna_seq = ''.join(seq_file.read().split())
    dna_seq = dna_seq.upper()
    seq_file.close()
    return dna_seq

compl_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def complement(seq):
    return ''.join(map(compl_dict.get,seq))

def revseq(seq):
    return ''.join(reversed(seq))

def reverseComplement(seq):
    return complement(revseq(seq))