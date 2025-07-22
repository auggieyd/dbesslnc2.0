import pandas as pd

# Reading files
lncbook = pd.read_csv('lncbook_conversion_results.csv')  # Contains ID, symbol, entrez
noncode = pd.read_csv('noncode_conversion_results.csv')  # Contains ID, symbol, entrez
merged_file = pd.read_csv('../statistic/lncRNA.csv')  # merged_file.csv should contain ID1, ID2, SomeColumn, symbol, and entrez initially empty

# Replace placeholders with NaN
lncbook.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'entrez': {'-': pd.NA, 'N/A': pd.NA}, 'ensembl_id': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)
noncode.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'entrez': {'-': pd.NA, 'N/A': pd.NA}, 'ensembl_id': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)
merged_file.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'entrez': {'-': pd.NA, 'N/A': pd.NA}, 'ensembl_id': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)

# Merge symbol and entrez based on lncbook
merged_file = pd.merge(merged_file, lncbook[['id', 'symbol', 'entrez', 'ensembl_id']], left_on='Lncbook_id', right_on='id', how='left')
merged_file.rename(columns={'symbol': 'symbol_lncbook', 'entrez': 'entrez_lncbook', 'ensembl_id': 'ensembl_id_lncbook'}, inplace=True)

# Merge symbol and entrez based on noncode
merged_file = pd.merge(merged_file, noncode[['id', 'symbol', 'entrez', 'ensembl_id']], left_on='Noncode_id', right_on='id', how='left')
merged_file.rename(columns={'symbol': 'symbol_noncode', 'entrez': 'entrez_noncode', 'ensembl_id': 'ensembl_id_noncode'}, inplace=True)

# Create final results DataFrame
final_output = pd.DataFrame({
    'Lncbook_id': merged_file['Lncbook_id'],
    'Noncode_id': merged_file['Noncode_id'],
    'lethal_count': merged_file['lethal_count'],
    'chr': merged_file['chr'],
    'start': merged_file['start'],
    'end': merged_file['end'],
    'strand': merged_file['strand'],
    'gene_name': merged_file['symbol_lncbook'].combine_first(merged_file['symbol_noncode']).fillna('-'),  # Merge and fill empty values
    'NCBI_id': merged_file['entrez_lncbook'].combine_first(merged_file['entrez_noncode']).fillna('-'),  # Merge and fill empty values
	'ensembl_id': merged_file['ensembl_id_lncbook'].combine_first(merged_file['ensembl_id_noncode']).fillna('-')
})

# Output results to CSV file
final_output.to_csv('lncRNA_with_etrez_symbol_ensembl.csv', index=False)
print("Merge completed, results have been saved to lncRNA_with_etrez_symbol_ensembl.csv")
