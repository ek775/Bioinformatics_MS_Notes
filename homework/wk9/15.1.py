##### Download the file proteomics.summary.tsv from the course data-directory
# - columns are genes; rows are samples; 
# - values are # of distinct peptides observed
##### Write a pandas-based program to 
# - determine the number of genes with at least two distinct peptides in all samples.
# - determine the number of genes with at least two distinct peptides in at least one sample.
# - Hint: Slide 21 contains the essential tricks

import pandas as pd

df = pd.read_csv('./proteomics.summary.tsv', sep='\t')
df.head()
df.info()
df.describe()

# number of genes(columns) with 2+ peptide variants in all 25 samples
genes_2p_all25 = []
for gene in df:
    samples = df[gene]
    if samples.min()>=2:
        genes_2p_all25.append(gene)
    else:
        continue
print("Number of genes with 2+ peptide variants in all 25 samples:")
print(len(genes_2p_all25))

# number of genes with 2+ peptide variants in 1+ sample
genes_2p_atl1 = []
for gene in df:
    samples = df[gene]
    if samples.max()>=2:
        genes_2p_atl1.append(gene)
    else:
        continue
print("Number of genes with 2+ peptide variants in at least 1 sample:")
print(len(genes_2p_atl1))