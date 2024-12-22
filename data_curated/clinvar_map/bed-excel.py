import pandas as pd

# File path
input_bed_file = 'db/redo/lncRNA_variant_nocrispr.bed'
output_csv_file = 'db/redo/lncRNA_variant_nocrispr.csv'

# Read the first line of the BED file as the header
with open(input_bed_file, 'r') as file:
    header_line = file.readline().strip()
    header = header_line.split('\t')

# Print the header for verification
print(f"Header: {header}")

# Read the data section of the BED file (skip the header line)
df = pd.read_csv(input_bed_file, sep='\t', header=None, skiprows=1, names=header, dtype=str)

# Print the shape and first few rows of the DataFrame for verification
print(f"DataFrame shape: {df.shape}")
print(df.head())

# Write the DataFrame to a CSV file
df.to_csv(output_csv_file, index=False)

print(f"Converted {input_bed_file} to {output_csv_file} successfully.")
