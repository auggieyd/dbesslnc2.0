import pandas as pd

file = 'crispr_variant_complete.csv'

df = pd.read_csv(file, sep=',', dtype=str)

# Convert 0-based coordinates to 1-based coordinates before storing data into the database
df['GenomicStartLoc'] = pd.to_numeric(df['GenomicStartLoc'], errors='coerce')
df['GenomicStartLoc'] = df['GenomicStartLoc'].fillna(0) + 1

df['chromStart'] = pd.to_numeric(df['chromStart'], errors='coerce')
df['chromStart'] = df['chromStart'].fillna(0) + 1

df = df[['ChromosomeName', 'GenomicStartLoc', 'GenomicEndLoc', 'GenomicStrand', 'target', 'chromStart', 'chromEnd', 'Type', 'ClinicalSignificance', 'VariationID',
         'ReferenceAlleleVCF', 'AlternateAlleleVCF', 'PhenotypeList']]

new_column_names = ['chr', 'start', 'end', 'strand', 'target', 'variant_start', 'variant_end', 'variant_type', 'clinical_significance', 'variation_id',
                    'reference_allele', 'alternate_allele', 'phenotype']

df.columns = new_column_names

# Filter rows where the ClinicalSignificance column contains "Likely pathogenic" or "Pathogenic"
df_filtered = df[df['clinical_significance'].str.contains('Likely pathogenic|Pathogenic', case=False, na=False)]

# 1. Generate a table for Likely pathogenic/Pathogenic variants
# Keep columns with mutation information
columns_to_keep_in_variant = ['chr', 'variant_start', 'variant_end', 'variant_type', 'clinical_significance',
                              'variation_id', 'reference_allele', 'alternate_allele', 'phenotype']
df_variant = df_filtered[columns_to_keep_in_variant]

# Remove duplicate VariationID values, keeping one row per mutation
df_variant_unique = df_variant.drop_duplicates(subset='variation_id')

# Save variants to a CSV file
variant_file = 'crispr_variants.csv'
df_variant_unique.to_csv(variant_file, index=False)

# 2. Generate lncRNA table with counts of pathogenic variants
# Group by ID and count qualifying mutations
variant_counts = df_filtered.groupby(['target']).size().reset_index(name='likely_or_pathogenic_count')

# Keep other relevant columns
columns_to_keep = ['target', 'chr', 'start', 'end', 'strand']
df_lncRNA = pd.merge(variant_counts, df[columns_to_keep].drop_duplicates(), on=['target'])

# Save lncRNA to a CSV file
lncRNA_file = 'crispr_lncRNA.csv'
df_lncRNA.to_csv(lncRNA_file, index=False)

# 3. Generate mapping table for variants and lncRNAs
# Keep only NoncodeID, LncBookID, and VariationID columns
variant_lncRNA_mapping = df_filtered[['target', 'variation_id']].drop_duplicates()

# Save the mapping table to a CSV file
variant_lncRNA_mapping_file = 'crispr_mapping.csv'
variant_lncRNA_mapping.to_csv(variant_lncRNA_mapping_file, index=False)

print("All tables have been successfully generated and saved.")
