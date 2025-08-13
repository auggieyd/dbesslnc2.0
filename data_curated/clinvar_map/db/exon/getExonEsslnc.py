import pandas as pd

# Read input files
lncRNA_file = pd.read_csv('dbesslnc_mapping.txt', sep='\t')
lncRNA_file = lncRNA_file[['Lncbook_id','Noncode_id','UID']]

lncbook_transcript_file = pd.read_csv('../../lncRNA_reference/LncBook/LncBookv2.0_lncRNA_transcripts.csv')  # LncBook transcript file
noncode_transcript_file = pd.read_csv('../../lncRNA_reference/NONCODE/NONCODEv6_lncRNA_transcripts.csv')  # Noncode transcript file

lncbook_transcript_file.columns=['Lncbook_id', 'Lncbook_trans_id', 'chr', 'start', 'end', 'strand', 'exon_num', 'exon_pos']
noncode_transcript_file.columns=['Noncode_id', 'NONCODE_TRANSCRIPT_ID', 'chr', 'start', 'end', 'strand', 'exon_num', 'exon_pos']

# Make a copy of the original DataFrame to avoid SettingWithCopyWarning
lncRNA_file = lncRNA_file.copy()

# Mask for rows where 'Lncbook_id' is NA
lncbook_lncRNA = lncRNA_file[lncRNA_file["Lncbook_id"] != "N.A."]

# Merge LncBook genes with LncBook transcript file
if not lncbook_lncRNA.empty: 
    lncbook_merged = pd.merge(
        lncbook_lncRNA,
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
noncode_lncRNA = lncRNA_file[lncRNA_file['Lncbook_id'] == "N.A."]
if not noncode_lncRNA.empty:
    noncode_merged = pd.merge(
        noncode_lncRNA,
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

# Save the result to a CSV file
final_merged.to_csv('dbesslnc_trans.csv', index=False)

print("Processing complete. Results have been saved to lncRNA_with_transcripts.csv.")
