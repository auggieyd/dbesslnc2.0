import pandas as pd
import sys

if len(sys.argv) > 1:
    db_name = sys.argv[1]

file = f'../../map/{db_name}_lncRNA_variant.bed'

df = pd.read_csv(file, sep='\t', dtype=str)

# Before inserting the data into the database, convert 0-based coordinates to 1-based coordinates
df['GenomicStartLoc'] = pd.to_numeric(df['GenomicStartLoc'], errors='coerce')
df['GenomicStartLoc'] = df['GenomicStartLoc'].fillna(0) + 1

df['chromStart'] = pd.to_numeric(df['chromStart'], errors='coerce')
df['chromStart'] = df['chromStart'].fillna(0) + 1

df = df[['ChromosomeName', 'GenomicStartLoc', 'GenomicEndLoc', 'GenomicStrand', 'ID', 'chromStart',
         'chromEnd', 'Type', 'ClinicalSignificance', 'VariationID', 'ReferenceAlleleVCF', 'AlternateAlleleVCF',
         'CompletePhenotypeList']]

new_column_names = ['chr', 'start', 'end', 'strand', 'lncRNA_id',
                    'variant_start', 'variant_end', 'variant_type', 'clinical_significance', 'variation_id',
                    'reference_allele', 'alternate_allele', 'phenotype']

df.columns = new_column_names

# 1. Generate lethal variants table
# Keep columns related to variant information
columns_to_keep_in_variant = ['chr', 'variant_start', 'variant_end', 'variant_type', 'clinical_significance',
                              'variation_id', 'reference_allele', 'alternate_allele', 'phenotype']
df_variant = df[columns_to_keep_in_variant]

# Remove duplicate VariationIDs, keeping one row per variant
df_variant_unique = df_variant.drop_duplicates(subset='variation_id')

# Save variants to a csv file
variant_file = f'{db_name}_variants.csv'
df_variant_unique.to_csv(variant_file, index=False)

# 2. Generate lncRNA table (lncRNA table with pathogenic variants counts)
# Group by ID and count the number of qualifying variants
variant_counts = df.groupby(['lncRNA_id']).size().reset_index(name='lethal_count')

# Keep other columns
columns_to_keep = ['lncRNA_id', 'chr', 'start', 'end', 'strand']
df_lncRNA = pd.merge(variant_counts, df[columns_to_keep].drop_duplicates(), on=['lncRNA_id'])

# Save lncRNA to CSV file
lncRNA_file = f'{db_name}_lncRNA.csv'
df_lncRNA.to_csv(lncRNA_file, index=False)

# 3. Generate variant to lncRNA mapping table
# Only keep NoncodeID, LncBookID, and VariationID columns
variant_lncRNA_mapping = df[['lncRNA_id', 'chr', 'start', 'end', 'strand', 'variation_id']].drop_duplicates()

# Save the mapping table to CSV file
variant_lncRNA_mapping_file = f'{db_name}_mapping.csv'
variant_lncRNA_mapping.to_csv(variant_lncRNA_mapping_file, index=False)

print("All tables have been successfully generated and saved.")
