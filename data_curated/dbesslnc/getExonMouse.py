import pandas as pd

# 1. Read input files
lncRNA_mouse = pd.read_csv('dbesslnc_mouse_trans.txt', sep='\t')  # lncRNA gene file
mouse_transcript_file = pd.read_csv('../../lncRNA_reference/NONCODE/NONCODEv6_mm10.transcript.csv')  # Noncode transcript file

# 2. Use Noncode_id to retrieve transcripts from Noncode
lncRNA_mouse['Lncbook_trans_id'] = "N.A."
mouse_merged = pd.merge(lncRNA_mouse, mouse_transcript_file, on='Noncode_trans_id', how='inner')

mouse_merged['transcript_id'] = mouse_merged['Noncode_trans_id']

# 3. Save the result to a CSV file
mouse_merged.to_csv('mouse_trans.csv', index=False)

print("Processing complete. Results have been saved to mouse_trans.csv.")
