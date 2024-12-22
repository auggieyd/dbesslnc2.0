import pandas as pd

# Reading files
file1 = pd.read_csv('lncbook_conversion_results.csv')  # Contains ID, symbol, entrez
file2 = pd.read_csv('noncode_conversion_results.csv')  # Contains ID, symbol, entrez
file3 = pd.read_csv('../map_results/lncRNA.csv')  # file3.csv should contain ID1, ID2, SomeColumn, symbol, and entrez initially empty

# Replace placeholders with NaN
file1.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'entrez': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)
file2.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'entrez': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)
file3.replace({'symbol': {'-': pd.NA, 'N/A': pd.NA}, 'entrez': {'-': pd.NA, 'N/A': pd.NA}}, inplace=True)

# Merge symbol and entrez based on file1
file3 = pd.merge(file3, file1[['id', 'symbol', 'entrez']], left_on='Lncbook_id', right_on='id', how='left')
file3.rename(columns={'symbol': 'symbol_file1', 'entrez': 'entrez_file1'}, inplace=True)

# Merge symbol and entrez based on file2
file3 = pd.merge(file3, file2[['id', 'symbol', 'entrez']], left_on='Noncode_id', right_on='id', how='left')
file3.rename(columns={'symbol': 'symbol_file2', 'entrez': 'entrez_file2'}, inplace=True)

# Create final results DataFrame
final_output = pd.DataFrame({
    'Lncbook_id': file3['Lncbook_id'],
    'Noncode_id': file3['Noncode_id'],
    'likely_or_pathogenic_count': file3['likely_or_pathogenic_count'],
    'chr': file3['chr'],
    'start': file3['start'],
    'end': file3['end'],
    'strand': file3['strand'],
    'gene_name': file3['symbol_file1'].combine_first(file3['symbol_file2']).fillna('-'),  # Merge and fill empty values
    'NCBI_id': file3['entrez_file1'].combine_first(file3['entrez_file2']).fillna('-')  # Merge and fill empty values
})

# Output results to CSV file
final_output.to_csv('lncRNA_with_etrez_symbol.csv', index=False)

print("Merge completed, results have been saved to lncRNA_with_etrez_symbol.csv")
