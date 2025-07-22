import pandas as pd

# Read UID file and origin mapping file
file1 = pd.read_csv('crispr_map.txt', sep='\t', header=0)
file2 = pd.read_csv('../crispr_map/crispr_mapping.csv', sep=',', header=0)

# Merge based on the key, then delete the key after merging.
merged_file = pd.merge(file2, file1, on='target', how='left')
merged_file = merged_file.drop(['target'], axis=1)

merged_file.to_csv('final_crispr_mapping.csv', index=False, sep=',')
