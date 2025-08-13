import pandas as pd
import re
import os

def process_ncbi_mappings_and_summaries(file_path, summary_file):
    """Read NCBI mapping files, extract gene IDs, and match gene summary information"""
    
    # Collect gene IDs
    all_gene_ids = set()
    
    df = pd.read_csv(file_path, sep='\t', header=None)
    if len(df.columns) >= 4:
        all_gene_ids.update(df.iloc[:, 3].dropna().unique())
    # Read gene summary file
    gene_summary_df = None
    gene_summary_df = pd.read_csv(summary_file, sep='\t')

    
    # Clean Summary column
    def clean_summary(summary):
        if pd.isna(summary):
            return ''
        return re.sub(r'\s*\[provided by.*$', '', str(summary), flags=re.IGNORECASE).strip()
    
    gene_summary_df['Summary_cleaned'] = gene_summary_df['Summary'].apply(clean_summary)
    
    # Match gene IDs and summaries
    results = []
    for gene_id in all_gene_ids:
        match = gene_summary_df[gene_summary_df['GeneID'] == gene_id]
        if not match.empty:
            summary = match.iloc[0]['Summary_cleaned']
            results.append({'GeneID': gene_id, 'Summary': summary})
    
    # Save results
    result_df = pd.DataFrame(results)
    result_df.to_csv('ncbi_gene_summaries.tsv', sep='\t', index=False)
    
    print(f"Completed: {len(all_gene_ids)} gene IDs, output file: ncbi_gene_summaries.tsv")

if __name__ == "__main__":
    process_ncbi_mappings_and_summaries()