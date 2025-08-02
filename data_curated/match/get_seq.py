import requests
import sys
import pandas as pd
import time

# Read the bed file,crispr_all.bed
input_bed = "./test/output/crispr_all.bed"
df = pd.read_csv(input_bed, sep='\t', header=None)
df.columns = ['chr', 'start', 'end', 'name', 'score', 'strand']
# df.columns = ['name', 'chr', 'start', 'end',  'strand']


df['key'] = df['name'].str.rsplit('-', n=1).str[0]
# df['key'] = df['name']

grouped = df.groupby('key').agg({
    'chr': 'first',
    'start': 'min',
    'end': 'max',
    'strand': 'first'
}).reset_index()

# 
grouped['start'] = grouped['start'] + 1

server = "https://rest.ensembl.org"
# grouped.to_csv('./test/output/crispr_gene.tsv', sep='\t', index=False, header=False)
# print(len(grouped))
with open('./test/output/crispr_gene.fa', 'a') as f:

    for _, row in grouped.iterrows():
        time.sleep(1)
        strand = "-1" if row['strand'] == '-' else "1"
        if '_' in row['chr']:
            continue
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