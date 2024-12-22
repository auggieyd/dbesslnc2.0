import requests
import sys
import pandas as pd
import time

# Read the bed file,crispr_all.bed
input_bed = "crispr_all.bed"
df = pd.read_csv(input_bed, sep='\t', header=None)
df.columns = ['chr', 'start', 'end', 'name', 'score', 'strand']


df['key'] = df['name'].str.rsplit('-', n=1).str[0]


grouped = df.groupby('key').agg({
    'chr': 'first',
    'start': 'min',
    'end': 'max',
    'strand': 'first'
}).reset_index()

# 
grouped['start'] = grouped['start'] + 1

server = "https://rest.ensembl.org"


with open('crispr_gene.fa', 'w') as f:
    
    for _, row in grouped.iterrows():
        time.sleep(1)
        strand = "-1" if row['strand'] == '-' else "1"
        ext = f"/sequence/region/human/{row['chr']}:{row['start']}..{row['end']}:{strand}?mask=soft"
        
        r = requests.get(server+ext, headers={"Content-Type": "text/x-fasta"})
        
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        
        sequence_lines = r.text.split('\n')
        header = sequence_lines[0].replace('>chromosome:GRCh38:', '')
        sequence = '\n'.join(sequence_lines[1:])
        
        f.write(f">{row['key']}:{header}\n")
        f.write(f"{sequence}\n")