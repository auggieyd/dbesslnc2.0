# Retain rows categorized as 'gene' and the required columns from NONCODEv6_hg38.lncAndGene.bed file
awk '$4 ~ /^NONHSAG/ {print $1 "\t" $2 "\t" $3 "\t" $4 "\t" $5 "\t" $6}' ./NONCODE/NONCODEv6_hg38.lncAndGene.bed > ./NONCODE/NONCODEv6_hg38.lncRNAGene.bed
# Retain rows categorized as 'gene' and the required columns from lncRNA_LncBookv2.0_GRCh38.gtf file, and convert to bed format
awk -F'\t' '$3 == "gene" {split($9, a, "\""); print $1 "\t" $4-1 "\t" $5 "\t" a[2] "\t" $6 "\t" $7}' ./LncBook/lncRNA_LncBookv2.0_GRCh38.gtf > ./LncBook/lncRNA_gene_LncBookv2.0_GRCh38.bed
