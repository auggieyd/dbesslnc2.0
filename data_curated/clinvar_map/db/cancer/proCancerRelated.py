import pandas as pd

# 1. Read files
lncRNA_cancer = pd.read_csv('cancer(2).txt', sep='\t')  # lncRNA gene file
mapping_file = pd.read_csv('gene_mapping.txt', sep='\t')
pos_file = pd.read_csv('../../lncRNA_reference/NONCODE_LncBook_same_merged.bed', sep='\t')

# 2. Read columns of interest
cols_lncRNA_lncbook = ['gene_name', 'ncbi_id']
lncbook_cancer = lncRNA_cancer[cols_lncRNA_lncbook]

mapping_file.columns = ['gene_name', 'LncBook_id']

pos_file.columns = ['chr', 'start', 'end', 'score', 'strand', 'Noncode_id', 'LncBook_id']
pos_file = pos_file[['chr', 'start', 'end', 'strand', 'Noncode_id', 'LncBook_id']]

# 3. Retrieve genomic positions based on gene name
lncbook_gene = pd.merge(lncbook_cancer, mapping_file, on='gene_name', how='inner')

lncbook_pos = pd.merge(lncbook_gene, pos_file, on='LncBook_id', how='inner')

# 5. Retrieve genomic positions based on NONCODE ID
noncode_cancer = lncRNA_cancer[['gene_name', 'ncbi_id', 'Noncode_id']]
noncode_cancer = noncode_cancer[~noncode_cancer['gene_name'].isin(lncbook_pos['gene_name'])]

if not noncode_cancer.empty:
    noncode_pos = pd.merge(noncode_cancer, pos_file, on='Noncode_id', how='inner')
    final_result = pd.concat([lncbook_pos, noncode_pos])
else:
    final_result = lncbook_pos

gene_remaining = lncRNA_cancer[~lncRNA_cancer['gene_name'].isin(final_result['gene_name'])]

# 6. Save to a CSV file
final_result.to_csv('cancer_related_lnc.csv', index=False)
gene_remaining.to_csv('dbesslnc_gene_remaining.csv', index=False)
print("Processing complete, results have been saved.")
