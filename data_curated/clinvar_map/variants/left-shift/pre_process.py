import pandas as pd
import csv
import re

# File paths
input_file = '../variant_summary.txt'
temp_output_file = 'variant_summary_GRCh38_filtered.csv'

# Read TXT file with tab as the delimiter
dtype = {18: str}
df = pd.read_csv(input_file, sep='\t', dtype=dtype)

# Filter out variants with fewer than 1 star or conflicting statuses
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
vcf_file = '../clinvar.vcf'
vcf_ids = set()

with open(vcf_file, 'r') as vcf:
    for line in vcf:
        if not line.startswith('#'):  # Skip comment lines
            columns = line.strip().split('\t')
            vcf_ids.add(columns[2])  # Third column is the ID column

# Filter df to keep rows where VariationID exists in the variants file IDs
df_filtered = df_filtered[df_filtered['VariationID'].astype(str).isin(vcf_ids)]

# Set to store RCVs whose conditions exceed 5
marked_rcvs = set()

# Function to replace "n conditions" with marker + corresponding RCV
def replace_condition_counts_with_marked_rcv(row):
    rcv_list = row['RCVaccession'].split('|')
    pheno_list = row['PhenotypeList'].split('|')

    new_pheno_list = []
    for rcv, pheno in zip(rcv_list, pheno_list):
        pheno = pheno.strip()
        if re.match(r'^\d+\s+conditions$', pheno):
            # Store the RCV for later export
            marked_rcvs.add(rcv.strip())
            # Replace with marked RCV
            new_pheno_list.append(f"RCV_MARK:{rcv.strip()}")
        else:
            new_pheno_list.append(pheno)
    
    return '|'.join(new_pheno_list)

# Apply the replacement function across the DataFrame
df_filtered['CleanedPhenotypeList'] = df_filtered.apply(replace_condition_counts_with_marked_rcv, axis=1)

# Write the marked RCVs to a .txt file (one per line, no header)
with open("marked_rcv_ids.txt", "w") as f:
    for rcv in sorted(marked_rcvs):
        f.write(rcv + "\n")

print(df_filtered.columns)
df_filtered.to_csv(temp_output_file, sep='\t', index=False)
