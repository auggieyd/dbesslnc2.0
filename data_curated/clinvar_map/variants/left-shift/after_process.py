import pandas as pd
import csv
import re

# File paths
variationID_length = 'variantID_length.csv'  # Temporary file to store ID and length
temp_file = 'variant_summary_GRCh38_filtered_pheno_completed.csv'
output_file = 'variant_summary_GRCh38_filtered_left_shift_length1.bed'

dtype = {18: str}
df_filtered = pd.read_csv(temp_file, sep='\t', dtype=dtype)

# Read lethal phenotypes from txt file (convert to lowercase for case-insensitive matching)
with open('lethal_phenotype.txt', 'r') as file:
    lethal_phenotypes = [line.strip().lower() for line in file]

def smart_split(phrase):
    """
    Smart split function: split by semicolon while ignoring semicolons inside parentheses.
    For example, "t(11;14) TYPE" should be treated as a single phenotype.
    """
    # Find all content inside parentheses
    bracket_content = re.findall(r'\(.*?\)', phrase)

    # Temporarily replace semicolons inside parentheses
    temp_phrase = phrase
    placeholder = "||SEMICOLON||"
    for content in bracket_content:
        temp_content = content.replace(';', placeholder)
        temp_phrase = temp_phrase.replace(content, temp_content, 1)

    # Split by semicolon safely
    parts = [p.strip() for p in temp_phrase.split(';') if p.strip()]

    # Restore original semicolons
    result = [part.replace(placeholder, ';') for part in parts]
    return result
 
def contains_lethal(phenotype_str):
    if not isinstance(phenotype_str, str):
        return False

    rcv_blocks = phenotype_str.split('|')

    for block in rcv_blocks:
        block = block.strip()
        for condition in smart_split(block):
            if condition.lower() in lethal_phenotypes:
                return True
    return False


# keep rows where PhenotypeList contains at least one lethal phenotype
df_filtered = df_filtered[df_filtered['CompletePhenotypeList'].apply(contains_lethal)]

# Map the length information from the dictionary to the DataFrame
length_dict = pd.read_csv(variationID_length, sep=',').set_index('VariationID')['VariantLength'].to_dict()
df_filtered['VariantLength'] = df_filtered['VariationID'].map(length_dict)

# Filter out variants longer than 100 bases or with unknown length
df_filtered = df_filtered.dropna(subset=['VariantLength'])
df_filtered = df_filtered[(df_filtered['VariantLength'].astype(int) <= 100) & (df_filtered['VariantLength'].astype(int) > 0)]
print(f"Filtered DataFrame row count: {len(df_filtered)}")

# Calculate the stop position for the variant
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
