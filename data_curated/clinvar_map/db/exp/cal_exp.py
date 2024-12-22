import pandas as pd

# 1. Read the TSV file
file_path = 'expression_profiles_HPA/HPATranscriptTPM.tsv'
df = pd.read_csv(file_path, sep='\t')

# 2. Create a dictionary to group columns by the same prefix
prefix_groups = {}

# 3. Iterate through column names and group them by prefix
for col in df.columns:
    prefix = col.split('_')[0]  # Prefix is the part before '_'
    if prefix not in prefix_groups:
        prefix_groups[prefix] = []
    prefix_groups[prefix].append(col)

# 4. Create a new DataFrame to store the calculated means
mean_df = pd.DataFrame()

# 5. Calculate the mean for each prefix group and name the mean column after the prefix
for prefix, columns in prefix_groups.items():
    if len(columns) > 1:  # Calculate mean only for groups with multiple columns
        mean_df[prefix] = df[columns].mean(axis=1)
    else:
        mean_df[prefix] = df[columns[0]]  # For a single column, use it directly

mean_df.columns.values[0] = 'Lncbook_trans_id'

# 6. Save the results to a new TSV file
mean_df.to_csv('expression_profiles_HPA/HPATranscriptTPM_MEAN.tsv', sep='\t', index=False)

print("Mean calculation completed and saved to HPATranscriptTPM_MEAN.tsv.")
