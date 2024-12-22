import pandas as pd

# Read the mapping file
id_mapping = {}
with open('NONCODE_LncBook_Map.txt') as f:
    for line in f:
        noncode_id, lnclook_id = line.strip().split()
        id_mapping[noncode_id] = lnclook_id

# Read the first BED file and create a dictionary
file1_data = pd.read_csv('../NONCODE/NONCODEv6_hg38.lncRNAGene_temp.bed', sep='\t', header=None)
file1_dict = []
file1_map_dict = {}
for _, row in file1_data.iterrows():
    if row[5] in id_mapping:
        key = row[5]
        file1_map_dict[key] = row
    else:
        file1_dict.append(row.tolist())

# Read and process the second BED file
file2_data = pd.read_csv('../LncBook/lncRNA_gene_LncBookv2.0_GRCh38_temp.bed', sep='\t', header=None)
merged_data = []

for _, row in file2_data.iterrows():
    matching_key = row[6]
    if matching_key in id_mapping.values():
        noncode_id = list(id_mapping.keys())[list(id_mapping.values()).index(matching_key)]
        if noncode_id in file1_map_dict:
            # Merge rows without additional processing
            merged_row = [row[0], row[1], row[2], row[3], row[4], noncode_id, matching_key]
            merged_data.append(merged_row)
            del file1_map_dict[noncode_id]
        else:
            merged_data.append(row.tolist())
    else:
        merged_data.append(row.tolist())

# Add unmatched rows from file1
print(file1_map_dict)
for remaining_row in file1_map_dict.values():
    merged_data.append(remaining_row.tolist())

merged_data = merged_data + file1_dict

# Save the final merged file
merged_df = pd.DataFrame(merged_data)
merged_df.to_csv('NONCODE_LncBook_same_merged.bed', sep='\t', header=False, index=False)
