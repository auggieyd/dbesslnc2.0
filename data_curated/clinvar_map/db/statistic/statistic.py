import pandas as pd

file = '../../map/lncRNA_variant_complete.bed'

df = pd.read_csv(file, sep='\t', dtype=str)
print(df.columns)

# Before inserting the data into the database, convert 0-based coordinates to 1-based coordinates
df['GenomicStartLoc'] = pd.to_numeric(df['GenomicStartLoc'], errors='coerce')
df['GenomicStartLoc'] = df['GenomicStartLoc'].fillna(0) + 1

df['chromStart'] = pd.to_numeric(df['chromStart'], errors='coerce')
df['chromStart'] = df['chromStart'].fillna(0) + 1

df = df[['ChromosomeName', 'GenomicStartLoc', 'GenomicEndLoc', 'GenomicStrand', 'NoncodeID', 'LncBookID', 'chromStart',
         'chromEnd', 'Type', 'ClinicalSignificance', 'VariationID', 'ReferenceAlleleVCF', 'AlternateAlleleVCF',
         'CompletePhenotypeList']]

new_column_names = ['chr', 'start', 'end', 'strand', 'Noncode_id', 'Lncbook_id',
                    'variant_start', 'variant_end', 'variant_type', 'clinical_significance', 'variation_id',
                    'reference_allele', 'alternate_allele', 'phenotype']

df.columns = new_column_names

# Filter rows where the 'ClinicalSignificance' column contains "Likely pathogenic" or "Pathogenic"
#df_filtered = df[df['clinical_significance'].str.contains('Likely pathogenic|Pathogenic', case=False, na=False)]

# 1. Generate lethal variants table
# Keep columns related to variant information
columns_to_keep_in_variant = ['chr', 'variant_start', 'variant_end', 'variant_type', 'clinical_significance',
                              'variation_id', 'reference_allele', 'alternate_allele', 'phenotype']
df_variant = df[columns_to_keep_in_variant]

# Remove duplicate VariationIDs, keeping one row per variant
df_variant_unique = df_variant.drop_duplicates(subset='variation_id')

# Save variants to a csv file
variant_file = 'variants.csv'
df_variant_unique.to_csv(variant_file, index=False)

# 2. Generate lncRNA table (lncRNA table with pathogenic variants counts)
# Group by ID and count the number of qualifying variants
variant_counts = df.groupby(['Noncode_id', 'Lncbook_id']).size().reset_index(name='lethal_count')

# Keep other columns
columns_to_keep = ['Noncode_id', 'Lncbook_id', 'chr', 'start', 'end', 'strand']
df_lncRNA = pd.merge(variant_counts, df[columns_to_keep].drop_duplicates(), on=['Noncode_id', 'Lncbook_id'])

# Save lncRNA to CSV file
lncRNA_file = 'lncRNA.csv'
df_lncRNA.to_csv(lncRNA_file, index=False)

# 3. Generate variant to lncRNA mapping table
# Only keep NoncodeID, LncBookID, and VariationID columns
variant_lncRNA_mapping = df[['Noncode_id', 'Lncbook_id', 'variation_id']].drop_duplicates()

# Save the mapping table to CSV file
variant_lncRNA_mapping_file = 'lncRNA_variant_mapping.csv'
variant_lncRNA_mapping.to_csv(variant_lncRNA_mapping_file, index=False)

print("All tables have been successfully generated and saved.")
