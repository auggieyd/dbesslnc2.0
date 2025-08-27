import pandas as pd

# Reading files
lncbook_outer_chain = pd.read_csv('lncbook_conversion_results.csv')  # Contains lncbookID, noncodeID, symbol, ncbi_id
noncode_outer_chain = pd.read_csv('noncode_conversion_results.csv')  # Contains lncbookID, noncodeID, symbol, ncbi_id
lncbook_lncRNA = pd.read_csv('../statistic/lncbook_lncRNA.csv')  
noncode_lncRNA = pd.read_csv('../statistic/noncode_lncRNA.csv')  
lncbook_mapping = pd.read_csv('../statistic/lncbook_mapping.csv')  
noncode_mapping = pd.read_csv('../statistic/noncode_mapping.csv')  

# Replace placeholders with NaN
lncbook_outer_chain.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'ncbi_id': {'-': pd.NA, 'N/A': pd.NA}, 'ensembl_id': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)
noncode_outer_chain.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'ncbi_id': {'-': pd.NA, 'N/A': pd.NA}, 'ensembl_id': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)

# Merge symbol ,ensembl_id ncbi_id based on lncbook
lncbook_merged_lncRNA = pd.merge(lncbook_outer_chain, lncbook_lncRNA, left_on='lncbook_id', right_on='lncRNA_id', how='right')
lncbook_merged_mapping = pd.merge(lncbook_outer_chain[['lncbook_id', 'noncode_id']], lncbook_mapping, left_on='lncbook_id', right_on='lncRNA_id', how='right')
lncbook_merged_lncRNA['lncbook_id'] = lncbook_merged_lncRNA['lncRNA_id']
lncbook_merged_mapping['lncbook_id'] = lncbook_merged_mapping['lncRNA_id']

# Merge symbol ,ensembl_id, ncbi_id based on noncode
noncode_merged_lncRNA = pd.merge(noncode_outer_chain, noncode_lncRNA, left_on='noncode_id', right_on='lncRNA_id', how='right')
noncode_merged_mapping = pd.merge(noncode_outer_chain[['lncbook_id', 'noncode_id']], noncode_mapping, left_on='noncode_id', right_on='lncRNA_id', how='right')
noncode_merged_lncRNA['noncode_id'] = noncode_merged_lncRNA['lncRNA_id']
noncode_merged_mapping['noncode_id'] = noncode_merged_mapping['lncRNA_id']

# Delete lncRNA_id 
del lncbook_merged_lncRNA['lncRNA_id']
del lncbook_merged_mapping['lncRNA_id']
del noncode_merged_lncRNA['lncRNA_id']
del noncode_merged_mapping['lncRNA_id']

# Output results to CSV file
lncbook_merged_lncRNA.to_csv('lncbook_lncRNA_with_outer_chain_info.csv', index=False)
noncode_merged_lncRNA.to_csv('noncode_lncRNA_with_outer_chain_info.csv', index=False)
lncbook_merged_mapping.to_csv('lncbook_mapping_with_outer_chain_info.csv', index=False)
noncode_merged_mapping.to_csv('noncode_mapping_with_outer_chain_info.csv', index=False)
