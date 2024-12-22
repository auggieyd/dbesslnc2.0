import pandas as pd
import csv

# File paths
variationID_length = 'variantID_length.csv'  # Temporary file to store ID and length
temp_file = 'variant_summary_GRCh38_filtered_temp.csv'
output_file = 'variant_summary_GRCh38_filtered_left_shift_length.bed'

dtype = {18: str}
df_filtered = pd.read_csv(temp_file, sep='\t', dtype=dtype)

# Map the length information from the dictionary to the DataFrame
length_dict = pd.read_csv(variationID_length, sep=',').set_index('VariationID')['VariantLength'].to_dict()
df_filtered['VariantLength'] = df_filtered['VariationID'].map(length_dict)

# Filter out mutations longer than 100 bases or with unknown length
df_filtered = df_filtered.dropna(subset=['VariantLength'])
df_filtered = df_filtered[(df_filtered['VariantLength'].astype(int) <= 100) & (df_filtered['VariantLength'].astype(int) > 0)]
print(f"Filtered DataFrame row count: {len(df_filtered)}")

# Calculate the stop position for the mutation
df_filtered['PositionVCF_Stop'] = df_filtered['PositionVCF'] + (df_filtered['Stop'] - df_filtered['Start'])

# Move chromosome and position columns to the first three columns
df_filtered = df_filtered[['Chromosome', 'PositionVCF', 'PositionVCF_Stop'] + [col for col in df_filtered.columns if col not in ['Chromosome', 'PositionVCF', 'PositionVCF_Stop']]]

# Adjust the start position to be 0-based
df_filtered['PositionVCF'] = df_filtered['PositionVCF'].astype(int) - 1

# Rename the first three columns
new_column_names = ['chrom', 'chromStart', 'chromEnd'] + [col for col in df_filtered.columns[3:]]

# Apply the new column names
df_filtered.columns = new_column_names

# Add 'chr' prefix to the chromosome column
df_filtered['chrom'] = df_filtered['chrom'].apply(lambda x: 'chr' + x if not x.startswith('chr') else x)

# Write the result to a new BED file with tab as the delimiter
df_filtered.to_csv(output_file, sep='\t', index=False, quoting=csv.QUOTE_NONE, escapechar='\\')
