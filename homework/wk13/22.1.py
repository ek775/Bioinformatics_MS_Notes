"""
Find potential fruit fly / yeast orthologs
Download FASTA files drosoph-ribosome.fasta.gz and yeast-ribosome.fasta.gz from the course data-directory.
Uncompress and format each FASTA file for BLAST
Search fruit fly ribosomal proteins against yeast ribosomal proteins
For each fruit fly query, output the best yeast protein if it has a significant E-value.
What ribosomal protein is most highly conserved between fruit fly and yeast?
"""

from Bio.Blast import NCBIXML
import pandas as pd
import sys

file = sys.argv[1]
assert type(file)==str
assert file[-4:]==".xml"

data = []
result_handle = open(file)
for blast_result in NCBIXML.parse(result_handle):
    for alignment in blast_result.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < 1e-5:
                dfi = pd.DataFrame({'accession':alignment.accession, 
                                    'hit_id':alignment.hit_id, 
                                    'hit_def': alignment.hit_def,
                                    'expect':hsp.expect, 
                                    'score':hsp.score, 
                                    'positives':hsp.positives, 
                                    'gaps':hsp.gaps}, 
                                    index=[0])
                data.append(dfi)
df = pd.concat(data, ignore_index=True)
print(df)

#find highly conserved proteins
print("Sorting by conservation...")
df = df.sort_values(by='score', axis=0, ascending=False)
print(df)
top_hit = df.iloc[0]

#export df as csv (more useful than printing)
print("Exporting data to CSV...")
out = f"{file[:-4]}.csv"
df.to_csv(out)
print(f"Data saved as {out}")

#return best conserved by score
print('---------------------------------')
print(f"Best Conserved Protein:")
print(top_hit)
