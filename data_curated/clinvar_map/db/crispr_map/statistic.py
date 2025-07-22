import pandas as pd

file = 'crispr_variant_complete.bed'

df = pd.read_csv(file, sep='\t', dtype=str)

# Convert 0-based coordinates to 1-based coordinates before storing data into the database
df['GenomicStartLoc'] = pd.to_numeric(df['GenomicStartLoc'], errors='coerce')
df['GenomicStartLoc'] = df['GenomicStartLoc'].fillna(0) + 1

df['chromStart'] = pd.to_numeric(df['chromStart'], errors='coerce')
df['chromStart'] = df['chromStart'].fillna(0) + 1

df = df[['ChromosomeName', 'GenomicStartLoc', 'GenomicEndLoc', 'GenomicStrand', 'Target', 'chromStart', 'chromEnd', 'Type', 'ClinicalSignificance', 'VariationID',
         'ReferenceAlleleVCF', 'AlternateAlleleVCF', 'PhenotypeList']]

new_column_names = ['chr', 'start', 'end', 'strand', 'target', 'variant_start', 'variant_end', 'variant_type', 'clinical_significance', 'variation_id',
                    'reference_allele', 'alternate_allele', 'phenotype']

df.columns = new_column_names

# 1. Generate lethal variants table
# Keep columns with variants information
columns_to_keep_in_variant = ['chr', 'variant_start', 'variant_end', 'variant_type', 'clinical_significance',
                              'variation_id', 'reference_allele', 'alternate_allele', 'phenotype']
df_variant = df[columns_to_keep_in_variant]

# Remove duplicate VariationID values, keeping one row per mutation
df_variant_unique = df_variant.drop_duplicates(subset='variation_id')

# Save variants to a CSV file
variant_file = 'crispr_variants.csv'
df_variant_unique.to_csv(variant_file, index=False)

# 2. Generate lncRNA table with counts of lethal variants
# Group by ID and count qualifying variants
variant_counts = df.groupby(['Target']).size().reset_index(name='lethal_count')

# Keep other relevant columns
columns_to_keep = ['Target', 'chr', 'start', 'end', 'strand']
df_lncRNA = pd.merge(variant_counts, df[columns_to_keep].drop_duplicates(), on=['Target'])

# Save lncRNA to a CSV file
lncRNA_file = 'crispr_lncRNA.csv'
df_lncRNA.to_csv(lncRNA_file, index=False)

# 3. Generate mapping table for variants and lncRNAs
# Keep only target and VariationID columns
variant_lncRNA_mapping = df[['target', 'variation_id']].drop_duplicates()

# Save the mapping table to a CSV file
variant_lncRNA_mapping_file = 'crispr_mapping.csv'
variant_lncRNA_mapping.to_csv(variant_lncRNA_mapping_file, index=False)

print("All tables have been successfully generated and saved.")
