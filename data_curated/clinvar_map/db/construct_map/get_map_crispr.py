import pandas as pd

# Read files 1 and 2 (assuming they are csv or tsv files)
file1 = pd.read_csv('crispr_UID.txt', sep='\t', header=0)
file2 = pd.read_csv('../crispr_map/crispr_mapping.csv', sep=',', header=0)

# Use merge for multi-column merging
merged_file = pd.merge(file2, file1[['target', 'UID']],
                       on=['target'], how='left')
# Remove unnecessary information
merged_file = merged_file.drop(['target'], axis=1)

# Save the results to a new file
merged_file.to_csv('crispr_mapping.csv', index=False, sep=',')

print("Merge completed, results saved to crispr_mapping.csv")
