import csv
import re
import pandas as pd
import os

def extract_ids(csv_file):
    with open("./test/crispr_casRx_id.txt", "r") as f:
        id_list = [line.strip() for line in f if line.strip()] 
        df = pd.read_csv(csv_file)
        matched_rows = df[df["LncRNA_family_ID"].isin(id_list)]  
        matched_rows.to_csv("temp_results.csv", index=False)  

def generate_bed(input_csv, supplementary_tsv, output_bed):
    """
    Process input data and generate a custom BED file.
    BED format columns (commonly used):
    1. Chromosome name (chr)
    2. Start position (start, 0-based)
    3. End position (end)
    4. Name/ID
    5. Score (usually .)
    6. Strand (+/-)
    7. Extra info 1
    8. Feature type (transcript/exon etc.)
    """
    # Read supplementary_table2.tsv to build mapping
    urs_info = {}
    with open(supplementary_tsv, 'r', encoding='utf-8') as tsv_f:
        tsv_reader = csv.reader(tsv_f, delimiter='\t')
        headers = next(tsv_reader)  # Skip header
        for row in tsv_reader:
            if len(row) < 5:
                continue  # Skip incomplete rows
            urs_id = row[0]
            # Store chromosome, start, end, strand
            urs_info[urs_id] = {
                'chr': row[1],
                'start': int(row[2]),  # Convert to int for processing
                'end': int(row[3]),
                'strand': row[4],
                'exon_sizes': row[6].split(',') if len(row) > 6 else [],
                'exon_offsets': row[7].split(',') if len(row) > 7 else []
            }
    
    # Process input CSV and generate BED content
    with open(input_csv, 'r', encoding='utf-8') as csv_f, \
         open(output_bed, 'w', encoding='utf-8') as bed_f:
        
        csv_reader = csv.reader(csv_f)
        for line_num, row in enumerate(csv_reader, 1):
            if len(row) < 3:
                print(f"Warning: Line {line_num} format incorrect, skipped")
                continue
            
            # Parse CSV data
            fused_id = row[0]  # e.g. human_lncrna_fused_7566
            transcript_str = row[1]
            status = row[2]
            
            # Split ID string (handle % and ~ as separators)
            transcript_ids = re.split(r'[%~#]', transcript_str)
            # Remove duplicates and filter empty values
            unique_ids = list(filter(None, set(transcript_ids)))
            
            # Match and generate BED lines
            for tid in unique_ids:
                if tid in urs_info:
                    info = urs_info[tid]
                    # Build main ID
                    main_id = f"{fused_id}-{tid}"
                    
                    # Generate transcript line
                    transcript_line = [
                        info['chr'],
                        str(info['start']),  # BED start is 0-based
                        str(info['end']),
                        main_id,
                        ".",  # Score
                        info['strand'],
                        fused_id,  # Extra info: fused ID
                        "transcript"  # Feature type
                    ]
                    bed_f.write('\t'.join(transcript_line) + '\n')
                    
                    # Generate exon lines (if exon info exists)
                    if len(info['exon_sizes']) == len(info['exon_offsets']) and len(info['exon_sizes']) > 0:
                        for i, (size, offset) in enumerate(zip(info['exon_sizes'], info['exon_offsets'])):
                            if not size or not offset:
                                continue
                            try:
                                exon_start = info['start'] + int(offset)
                                exon_end = exon_start + int(size)
                                exon_line = [
                                    info['chr'],
                                    str(exon_start),
                                    str(exon_end),
                                    f"{main_id}",  # Exon ID
                                    ".",
                                    info['strand'],
                                    fused_id,
                                    "exon"
                                ]
                                bed_f.write('\t'.join(exon_line) + '\n')
                            except ValueError:
                                print(f"Warning: Exon data format error - exon {i+1} of {tid}")
    
    print(f"Custom BED file generated: {output_bed}")

if __name__ == "__main__":
    # File paths
    INPUT_CSV = "temp_results.csv"         # Input CSV file
    SUPPLEMENTARY_TSV = "./test/Supplementary_table2.tsv"  # Supplementary table
    OUTPUT_BED = "./test/output/crispr_casrx_all.bed"            # Output BED file
    
    # Run generation
    extract_ids("./test/Supplementary_table4.csv")
    generate_bed(INPUT_CSV, SUPPLEMENTARY_TSV, OUTPUT_BED)
    os.system("awk 'NF{NF-=2}1' ./test/output/crispr_casrx_all.bed > ./test/output/crispr_casrx38.bed")
    os.system("rm temp_results.csv")
