import pandas as pd

# Read UID file and origin mapping file
file1 = pd.read_csv('disease_map.txt', sep='\t', header=0)
file2 = pd.read_csv('../crispr_overlap/lncRNA_variant_mapping_nocrispr.csv', sep=',', header=0)

# Merge based on the key, then delete the key after merging.
merged_file = pd.merge(file2, file1, on=['Lncbook_id', 'Noncode_id'], how='left')
merged_file = merged_file.drop(['Lncbook_id', 'Noncode_id'], axis=1)

merged_file.to_csv('final_nocrispr_mapping.csv', index=False, sep=',')
