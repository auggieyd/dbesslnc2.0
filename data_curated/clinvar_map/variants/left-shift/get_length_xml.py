import pandas as pd
import csv
import xml.etree.ElementTree as ET

temp_file = 'variant_summary_GRCh38_filtered_temp.csv'
variationID_length = 'variantID_length.csv'  # Temporary file to store ID and length

# Read the temporary file with tab as the delimiter
dtype = {18: str}
df_filtered = pd.read_csv(temp_file, sep='\t', dtype=dtype)

# Extract VariationID from df_filtered, deduplicate, and store in a set
variation_ids = set(df_filtered['VariationID'].astype(str))

# XML file path
xml_file = '../ClinVarVCVRelease_2024-0902.xml'

# Use iterparse to parse the XML file incrementally and store VariationID and VariantLength
context = ET.iterparse(xml_file, events=("start", "end"))  # Incremental XML parsing
parent_stack = []  # Use a stack to keep track of parent nodes

print('Starting XML parsing')
with open(variationID_length, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['VariationID', 'VariantLength'])  # Write the CSV header
    for event, elem in context:

        if event == "start":
            # For start events, push the element onto the stack
            parent_stack.append(elem)
        elif event == "end":
            if elem.tag == "SequenceLocation":
                # Check if the Assembly attribute is GRCh38
                if elem.get("Assembly") == "GRCh38":
                    # Get the parent SimpleAllele node
                    simple_allele = parent_stack[-3] if len(parent_stack) >= 3 else None
                    if simple_allele is not None:
                        variation_id = simple_allele.get("VariationID")  # Get VariationID
                        if variation_id in variation_ids:
                            variant_length = elem.get("variantLength")  # Get variantLength
                            if variant_length:
                                writer.writerow([variation_id, int(variant_length)])

            # Clear processed elements to prevent excessive memory usage
            elem.clear()
            parent_stack.pop()  # Pop the finished element from the stack

print('XML parsing completed, results saved to CSV file')
