import pandas as pd

# 1. Read input files
lncRNA_file = pd.read_csv('non_crispr_UID.txt', sep='\t')  # lncRNA gene file
lncbook_transcript_file = pd.read_csv('../../lncRNA_reference/LncBook/LncBookv2.0_lncRNA_transcripts.csv')  # LncBook transcript file
noncode_transcript_file = pd.read_csv('../../lncRNA_reference/NONCODE/NONCODEv6_lncRNA_transcripts.csv')  # Noncode transcript file

lncbook_transcript_file.columns=['Lncbook_id', 'Lncbook_trans_id', 'chr', 'start', 'end', 'strand', 'exon_num', 'exon_pos']
noncode_transcript_file.columns=['Noncode_id', 'NONCODE_TRANSCRIPT_ID', 'chr', 'start', 'end', 'strand', 'exon_num', 'exon_pos']


# 2. Extract columns of interest
lncRNA_cols_of_interest = ['Lncbook_id', 'Noncode_id', 'gene_name', 'UID']

lncRNA_file = lncRNA_file[lncRNA_cols_of_interest]

# 3. Use Lncbook_id to retrieve corresponding transcripts from LncBook
lncbook_gene = lncRNA_file[lncRNA_file['Lncbook_id'] != "N.A."]
lncbook_gene.loc[:, 'NONCODE_TRANSCRIPT_ID'] = ""
lncbook_merged = pd.merge(lncbook_gene, lncbook_transcript_file, on='Lncbook_id', how='inner')
print(lncbook_merged.columns.values)

# 4. For genes without LncBook_id, use Noncode_id to retrieve transcripts from Noncode
noncode_gene = lncRNA_file[lncRNA_file['Lncbook_id'] == "N.A."]
noncode_gene.loc[:, 'Lncbook_trans_id'] = ""
noncode_merged = pd.merge(noncode_gene, noncode_transcript_file, on='Noncode_id', how='inner')
print(noncode_merged.columns.values)

# 5. Combine results from both matches
final_merged = pd.concat([lncbook_merged, noncode_merged], ignore_index=True)
final_merged['Organism'] = 'Human'

# 6. Save the result to a CSV file
final_merged.to_csv('non_crispr_lncRNA.csv', index=False)

print("Processing complete. Results have been saved to lncRNA_with_transcripts.csv.")
