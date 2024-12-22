import pandas as pd
import csv

# File paths
input_file = '../variant_summary.txt'
temp_output_file = 'variant_summary_GRCh38_filtered_temp.csv'

# Read TXT file with tab as the delimiter
dtype = {18: str}
df = pd.read_csv(input_file, sep='\t', dtype=dtype)

# Filter out mutations with fewer than 1 star or conflicting statuses
valid_review_status = [
    'no assertion criteria provided',
    'criteria provided, conflicting classifications',
    'no classification provided',
    'no classification for the single variant',
    'no classifications from unflagged records'
]
df_filtered = df[~df['ReviewStatus'].isin(valid_review_status)]

# Keep only rows where the Assembly column value is 'GRCh38'
df_filtered = df_filtered[df_filtered['Assembly'] == 'GRCh38']

# Read variants file and extract the third column (ID column)
vcf_file = '../clinvar_20240603.vcf'
vcf_ids = set()

with open(vcf_file, 'r') as vcf:
    for line in vcf:
        if not line.startswith('#'):  # Skip comment lines
            columns = line.strip().split('\t')
            vcf_ids.add(columns[2])  # Third column is the ID column

# Filter df to keep rows where VariationID exists in the variants file IDs
df_filtered = df_filtered[df_filtered['VariationID'].astype(str).isin(vcf_ids)]

# Ensure the final DataFrame columns match the initial DataFrame
df_filtered = df_filtered[df.columns]
df_filtered.to_csv(temp_output_file, sep='\t', index=False, quoting=csv.QUOTE_NONE, escapechar='\\')
