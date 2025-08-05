import pandas as pd
import numpy as np
import os
import argparse

def process_new_matches(input_file, output_file):
    """
    Process new match results and select the optimal gene according to previous rules.
    """
    
    try:
        column_names = ['chr1', 'start1', 'end1', 'ID', 'score1', 'strand1', 
                        'chr2', 'start2', 'end2', 'name', 'score2', 'strand2',
                        'gene_id', 'transcript_id', 'feature', 'gene_name', 'gene_type', 'GeneID', 'overlap_length']

        df = pd.read_csv(input_file, sep='\t', header=None, names=column_names, low_memory=False, dtype=str)
        df['overlap_length'] = pd.to_numeric(df['overlap_length'], errors='coerce')
        df['start1'] = pd.to_numeric(df['start1'], errors='coerce') 
        df['end1'] = pd.to_numeric(df['end1'], errors='coerce')
        df['start2'] = pd.to_numeric(df['start2'], errors='coerce')
        df['end2'] = pd.to_numeric(df['end2'], errors='coerce')
        # print(f"Number of rows in new match data: {len(df)}")
        
        if len(df) == 0:
            print("No new match data")
            return
            
    except FileNotFoundError:
        print("Error: File not found")
        return
    
    # Create target columns
    df['target'] = df['ID'].str.rsplit('-', n=1).str[0]
    df['target_trans'] = df['ID'].str.rsplit('-', n=1).str[1]
    
    # print(f"Number of new targets: {df['target'].nunique()}")
    
    # Prefer genes not starting with LOC 
    # Prefer genes not starting with LOC (only in specific conflict cases)
    def prefer_non_loc_genes(df):
        # print("Checking gene_id conflicts, only handling LOC/non-LOC mixed conflicts...")

        filtered_records = []
        conflict_summary = []

        for target, group in df.groupby('target'):
            unique_gene_ids = group['gene_id'].dropna().unique()

            if len(unique_gene_ids) <= 1:
                # No conflict, keep all records
                filtered_records.append(group)
            else:
                # Conflict exists, check if it's a LOC/non-LOC mixed conflict
                loc_genes = [g for g in unique_gene_ids if str(g).startswith('LOC')]
                non_loc_genes = [g for g in unique_gene_ids if not str(g).startswith('LOC')]

                # Only prioritize when both LOC and non-LOC genes exist
                if len(loc_genes) > 0 and len(non_loc_genes) > 0:
                    # LOC/non-LOC mixed conflict, prefer non-LOC gene
                    selected_gene = non_loc_genes[0]  # Select the first non-LOC gene
                    reason = 'LOC/non-LOC mixed conflict, prefer non-LOC gene'

                    conflict_summary.append({
                        'target': target,
                        'all_genes': list(unique_gene_ids),
                        'loc_genes': loc_genes,
                        'non_loc_genes': non_loc_genes,
                        'selected_gene': selected_gene,
                        'reason': reason,
                        'rejected_genes': [g for g in unique_gene_ids if g != selected_gene]
                    })

                    # Keep only records for the selected gene
                    selected_records = group[group['gene_id'] == selected_gene]
                    filtered_records.append(selected_records)

                else:
                    # Other types of conflicts (all LOC or all non-LOC), keep all records, will select by exon length later
                    filtered_records.append(group)
                    # print(f"Target {target} has gene ID conflict but not LOC/non-LOC mixed, will select by exon length: {list(unique_gene_ids)}")

        if conflict_summary:
            # print(f"Handled {len(conflict_summary)} LOC/non-LOC mixed conflicts")

            # Save LOC conflict resolution report
            conflict_df = pd.DataFrame(conflict_summary)
            file_exists = os.path.isfile('loc_gene_conflict_resolution.csv')
            conflict_df.to_csv('loc_gene_conflict_resolution.csv', mode='a', header=not file_exists, index=False)
            # print("✓ LOC conflict resolution report saved: loc_gene_conflict_resolution.csv")
        else:
            print("No LOC/non-LOC mixed conflicts found")

        # Merge all filtered records
        return pd.concat(filtered_records, ignore_index=True) if filtered_records else pd.DataFrame()
    
    # Apply gene priority filtering
    df_filtered = prefer_non_loc_genes(df)
    
    if len(df_filtered) == 0:
        print("No data after filtering")
        return
    
    # Select the optimal gene based on cumulative exon length and return complete records
    def select_best_gene_by_exon_length(df):
        
        # Create coordinate field for deduplication
        df['coord_key'] = (df['chr2'].astype(str) + '_' + 
                           df['start2'].astype(str) + '_' + 
                           df['end2'].astype(str) + '_' + 
                           df['strand2'].astype(str))
        
        # Step 1: Calculate cumulative exon length for each target-gene_id combination
        length_summary_list = []
        
        for (target, geneid, gene_id), group in df.groupby(['target', 'GeneID', 'gene_id']):
            # Only calculate cumulative length from exon records
            exon_records = group[group['feature'] == 'exon']
            if len(exon_records) > 0:
                # Deduplicate by coordinates (only for exon records)
                unique_exon_coords = exon_records.drop_duplicates(subset=['coord_key'])
                # Calculate total length after deduplication
                total_length = unique_exon_coords['overlap_length'].sum()
            else:
                # If no exon records, use all records to calculate length
                unique_coords = group.drop_duplicates(subset=['coord_key'])
                total_length = unique_coords['overlap_length'].sum()

            gene_start = int(group['start2'].min())
            gene_end = int(group['end2'].max())
            gene_region_length = gene_end - gene_start

            coverage_ratio = total_length / gene_region_length if gene_region_length > 0 else 0
            
            length_summary_list.append({
                'target': target,
                'GeneID': geneid,
                'gene_id': gene_id,
                'total_exon_length': total_length,
                'coverage_ratio': coverage_ratio,
            })
        
        length_summary = pd.DataFrame(length_summary_list)
        # print(f"Number of target-gene combinations: {len(length_summary)}")
        
        # Step 2: Select the combination with the largest cumulative length for each target
        selected_combinations = []
        print(f"{len(length_summary.groupby('target'))} primary groups found")
        for target, group in length_summary.groupby('target'):
            # Select the combination with the largest cumulative length
            best_match = group.sort_values(['total_exon_length', 'coverage_ratio'], 
                                     ascending=[False, False]).iloc[0]
            selected_combinations.append({
                'target': best_match['target'],
                'selected_GeneID': best_match['GeneID'],
                'selected_gene_id': best_match['gene_id'],
                'total_exon_length': best_match['total_exon_length'],
                'coverage_ratio': best_match['coverage_ratio']
                
            })
        
        selected_df = pd.DataFrame(selected_combinations)
        
        # Step 3: Extract all related records from the original data according to the selected gene
        final_records = []
        
        for _, selection in selected_df.iterrows():
            target = selection['target']
            selected_geneid = selection['selected_GeneID']
            selected_gene_id = selection['selected_gene_id']
            
            # Find all records for the selected gene of the target from the original data
            matching_records = df[
                (df['target'] == target) & 
                (df['GeneID'] == selected_geneid) & 
                (df['gene_id'] == selected_gene_id)
            ]
            
            final_records.append(matching_records)
        
        # Merge all selected records
        return pd.concat(final_records, ignore_index=True) if final_records else pd.DataFrame()
    
    # Select the best gene and get complete records
    selected_records = select_best_gene_by_exon_length(df_filtered)
    
    # Filter out rows with empty GeneID
    selected_records = selected_records[selected_records['GeneID'].notna() & (selected_records['GeneID'] != '')]
    
    
    if len(selected_records) > 0:
        # Output in gencode_map.tsv format: target, target_trans, transcript_id, gene_id, gene_id, feature
        output_records = selected_records[['target', 'target_trans', 'transcript_id', 'GeneID', 'gene_id', 'feature']].drop_duplicates().copy()
        output_records.to_csv(output_file, sep='\t', header=False, index=False)
        
        print(f"✓ output: {output_file}")
    else:
        print("no records to output")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process new matches and update gene mapping.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the updated mapping output file")
    args = parser.parse_args()

    process_new_matches(args.input_file, args.output_file)