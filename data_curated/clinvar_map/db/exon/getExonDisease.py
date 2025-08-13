import pandas as pd

# Read input files
UID_file = pd.read_csv('../construct_map/variants_mapping.txt', sep='\t')
UID_file.replace({'Lncbook_id': {'N.A.': pd.NA}, 'Noncode_id': {'N.A.': pd.NA}}, inplace=True)

lncRNA_file = pd.read_csv('../construct_map/unique_lncRNA.csv')
lncbook_transcript_file = pd.read_csv('../../lncRNA_reference/LncBook/LncBookv2.0_lncRNA_transcripts.csv')  # LncBook transcript file
noncode_transcript_file = pd.read_csv('../../lncRNA_reference/NONCODE/NONCODEv6_lncRNA_transcripts.csv')  # Noncode transcript file

lncRNA_file = lncRNA_file[['lncbook_id','noncode_id','chr','start','end','strand','source']]
lncRNA_file.columns = ['Lncbook_id','Noncode_id','chr','start','end','strand','source']
lncbook_transcript_file.columns=['Lncbook_id', 'Lncbook_trans_id', 'chr', 'start', 'end', 'strand', 'exon_num', 'exon_pos']
noncode_transcript_file.columns=['Noncode_id', 'NONCODE_TRANSCRIPT_ID', 'chr', 'start', 'end', 'strand', 'exon_num', 'exon_pos']

UID_lncRNA = pd.merge(UID_file, lncRNA_file, on=['Lncbook_id','Noncode_id','chr','start','end','strand'], how = 'right')

# Extract columns of interest
lncRNA_cols_of_interest = ['Lncbook_id', 'Noncode_id', 'UID', 'source']

UID_lncRNA = UID_lncRNA[lncRNA_cols_of_interest]

# Make a copy of the original DataFrame to avoid SettingWithCopyWarning
UID_lncRNA = UID_lncRNA.copy()

# Mask for rows where 'source' contains 'lncbook' (case-insensitive)
lncbook_mask = UID_lncRNA["source"].str.contains("lncbook", case=False, na=False)

# Merge LncBook genes with LncBook transcript file
lncbook_gene = UID_lncRNA[lncbook_mask].copy()
if not lncbook_gene.empty: 
    lncbook_merged = pd.merge(
        lncbook_gene,
        lncbook_transcript_file,
        on="Lncbook_id",
        how="inner"
    )
    lncbook_merged["NONCODE_TRANSCRIPT_ID"] = ""
    lncbook_merged["transcript_id"] = lncbook_merged["Lncbook_trans_id"]
    print("LncBook merged columns:", lncbook_merged.columns.values)
else:
    lncbook_merged = pd.DataFrame()
    print("No LncBook genes found.")

# Merge Noncode genes with Noncode transcript file
noncode_gene = UID_lncRNA[~lncbook_mask].copy()
if not noncode_gene.empty:
    noncode_merged = pd.merge(
        noncode_gene,
        noncode_transcript_file,
        on="Noncode_id",
        how="inner"
    )
    noncode_merged["Lncbook_trans_id"] = ""
    noncode_merged["transcript_id"] = noncode_merged["NONCODE_TRANSCRIPT_ID"]
    print("Noncode merged columns:", noncode_merged.columns.values)
else:
    noncode_merged = pd.DataFrame()
    print("No Noncode genes found.")


# Combine results from both matches
final_merged = pd.concat([lncbook_merged, noncode_merged], ignore_index=True)
final_merged['Organism'] = 'Human'
final_merged.drop(['source'], axis=1, inplace=True)

# Save the result to a CSV file
final_merged.to_csv('disease_trans.csv', index=False)

print("Processing complete. Results have been saved to lncRNA_with_transcripts.csv.")
