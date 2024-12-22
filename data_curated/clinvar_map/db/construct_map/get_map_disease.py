import pandas as pd

# Read files 1 and 2 (assuming they are csv or tsv files)
file1 = pd.read_csv('disease_related_UID.txt', sep='\t', header=0)
file2 = pd.read_csv('../crispr_overlap/lncRNA_variant_mapping_nocrispr.csv', sep=',', header=0)

# Use merge for multi-column merging
merged_file = pd.merge(file2, file1[['Lncbook_id', 'Noncode_id', 'UID']],
                       left_on=['Lncbook_id', 'Noncode_id',], right_on=['Lncbook_id', 'Noncode_id',], how='left')
# Remove unnecessary information
merged_file = merged_file.drop(['Lncbook_id', 'Noncode_id'], axis=1)

# Save the results to a new file
merged_file.to_csv('final_lncRNA_variant_mapping.csv', index=False, sep=',')

print("Merge completed, results saved to final_lncRNA_variant_mapping.csv")
