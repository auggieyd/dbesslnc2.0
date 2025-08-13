import pandas as pd

# Read UID file and origin mapping file
UID_file = pd.read_csv('variants_mapping.txt', sep='\t')
mapping_file = pd.read_csv('unique_mapping.csv', sep=',')
mapping_file.columns = ['Lncbook_id', 'Noncode_id', 'chr', 'start', 'end', 'strand', 'variation_id']
UID_file.replace({'Lncbook_id': {'N.A.': pd.NA}, 'Noncode_id': {'N.A.': pd.NA}}, inplace=True)

# Merge based on the key, then delete the key after merging.
merged_file = pd.merge(UID_file, mapping_file, on=['Lncbook_id', 'Noncode_id', 'chr', 'start', 'end', 'strand'], how='right')
merged_file = merged_file.drop(['Lncbook_id', 'Noncode_id', 'chr', 'start', 'end', 'strand'], axis=1)

merged_file.to_csv('final_mapping.csv', index=False, sep=',')
