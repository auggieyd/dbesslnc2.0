import pandas as pd
import csv
import re

temp_file = 'variant_summary_GRCh38_filtered.csv'
output_file = 'variant_summary_GRCh38_filtered_pheno_completed.csv'

dtype = {18: str}
df_filtered = pd.read_csv(temp_file, sep='\t', dtype=dtype)

# Load the RCV-to-conditions map from a text file
def load_rcv_condition_map(file_path):
    rcv_map = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                rcv_id, condition = parts
                rcv_map[rcv_id.strip()] = condition.strip()
    return rcv_map


# Replace RCV_MARK entries using the loaded map
def substitute_rcv_markers(row, rcv_condition_map):
    pheno_list = row['CleanedPhenotypeList'].split('|')
    substituted_list = []

    for item in pheno_list:
        match = re.match(r'^RCV_MARK:(RCV\d+)$', item.strip())
        if match:
            rcv = match.group(1)
            # Replace with mapped condition or fallback text if not found
            condition = rcv_condition_map.get(rcv, f"UNMAPPED:{rcv}")
            substituted_list.append(condition)
        else:
            substituted_list.append(item.strip())
    
    return '|'.join(substituted_list)

# Load the map file
map_file_path = 'rcv_conditions.txt'  # path to your map file
rcv_condition_map = load_rcv_condition_map(map_file_path)

# Apply to DataFrame
df_filtered['CompletePhenotypeList'] = df_filtered.apply(
    lambda row: substitute_rcv_markers(row, rcv_condition_map), axis=1
)

df_filtered.to_csv(output_file, sep='\t', index=False, quoting=csv.QUOTE_NONE, escapechar='\\')

def smart_split(phrase):
    """
    Smart split function: split by semicolon while ignoring semicolons inside parentheses.
    For example, "t(11;14) TYPE" should be treated as a single phenotype.
    """
    # Find all content inside parentheses
    bracket_content = re.findall(r'\(.*?\)', phrase)

    # Temporarily replace semicolons inside parentheses
    temp_phrase = phrase
    placeholder = "||SEMICOLON||"
    for content in bracket_content:
        temp_content = content.replace(';', placeholder)
        temp_phrase = temp_phrase.replace(content, temp_content, 1)

    # Split by semicolon safely
    parts = [p.strip() for p in temp_phrase.split(';') if p.strip()]

    # Restore original semicolons
    result = [part.replace(placeholder, ';') for part in parts]
    return result

def extract_unique_phenotypes(df, column_name='CompletePhenotypeList'):
    """
    Extract unique phenotype terms from a DataFrame column.
    Each cell can contain multiple phenotype groups separated by "|", 
    and each group can contain sub-phenotypes separated by semicolons (some inside parentheses).
    """
    unique_phenotypes = set()
    row_count = 0

    for val in df[column_name]:
        row_count += 1
        if not isinstance(val, str) or not val.strip():
            continue
        
        # Step 1: Split by '|'
        groups = val.split('|')
        
        for group in groups:
            group = group.strip()
            if not group:
                continue

            # Smart split on semicolons
            phenotypes = smart_split(group)

            for phenotype in phenotypes:
                if phenotype:
                    unique_phenotypes.add(phenotype)

    # Sort the result
    sorted_phenotypes = sorted(unique_phenotypes)

    print(f"Input rows processed: {row_count}")
    print(f"Number of unique phenotypes extracted: {len(unique_phenotypes)}")

    return sorted_phenotypes

unique_phenotype_list = extract_unique_phenotypes(df_filtered)

# write to text file
output_file = "unique_phenotypes.txt"
with open(output_file, 'w', encoding='utf-8') as f:
	for phenotype in unique_phenotype_list:
		f.write(phenotype + '\n')
