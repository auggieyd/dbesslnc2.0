import pandas as pd

lncbook_lncRNA = pd.read_csv('../conversion/lncbook_lncRNA_with_outer_chain_info.csv', dtype=str)  
noncode_lncRNA = pd.read_csv('../conversion/noncode_lncRNA_with_outer_chain_info.csv', dtype=str) 

lncbook_lncRNA['source'] = 'lncbook'
noncode_lncRNA['source'] = 'noncode'
lncRNA = pd.concat([lncbook_lncRNA, noncode_lncRNA], ignore_index=True)

def join_sources(s, sep=";"):
    seen = set()
    out = []
    for val in s.dropna().astype(str):
        # in case some rows already contain multiple sources like "a;b"
        for part in (p.strip() for p in val.split(sep)):
            if part and part not in seen:
                seen.add(part)
                out.append(part)
    return sep.join(out) if out else ""

unique_lncRNA = (
    lncRNA
    .groupby(['lncbook_id','noncode_id','symbol','ncbi_id','lethal_count','chr','start','end','strand'], dropna=False, as_index=False)  # one row per unique combo of other columns
    .agg(source=('source', join_sources))     # merge sources with ';', remove duplicates (order-preserving)
)

unique_lncRNA.to_csv("unique_lncRNA.csv", index=False)

lncbook_mapping = pd.read_csv('../conversion/lncbook_mapping_with_outer_chain_info.csv')  
noncode_mapping = pd.read_csv('../conversion/noncode_mapping_with_outer_chain_info.csv') 

mapping = pd.concat([lncbook_mapping, noncode_mapping], ignore_index=True)
unique_mapping = mapping.drop_duplicates()
unique_mapping.to_csv("unique_mapping.csv", index=False)

lncbook_variants = pd.read_csv('../statistic/lncbook_variants.csv')  
noncode_variants = pd.read_csv('../statistic/noncode_variants.csv') 

variants = pd.concat([lncbook_variants, noncode_variants], ignore_index=True)
unique_variants = variants.drop_duplicates()
unique_variants.to_csv("unique_variants.csv", index=False)