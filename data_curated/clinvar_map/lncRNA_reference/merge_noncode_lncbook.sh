# Retain rows categorized as 'gene' and the required columns from NONCODEv6_hg38.lncAndGene.bed file
awk '$4 ~ /^NONHSAG/ {print $1 "\t" $2 "\t" $3 "\t" $4 "\t" $5 "\t" $6}' ./NONCODE/NONCODEv6_hg38.lncAndGene.bed > ./NONCODE/NONCODEv6_hg38.lncRNAGene.bed
awk '$4 ~ /^NONMMUG/ {print $1 "\t" $2 "\t" $3 "\t" $4 "\t" $5 "\t" $6}' ./NONCODE/NONCODEv6_mm10.lncAndGene.bed > ./NONCODE/NONCODEv6_mm10.lncRNAGene.bed
# Retain rows categorized as 'gene' and the required columns from lncRNA_LncBookv2.0_GRCh38.gtf file, and convert to bed format
awk -F'\t' '$3 == "gene" {split($9, a, "\""); print $1 "\t" $4-1 "\t" $5 "\t" a[2] "\t" $6 "\t" $7}' ./LncBook/lncRNA_LncBookv2.0_GRCh38.gtf > ./LncBook/lncRNA_gene_LncBookv2.0_GRCh38.bed
# Use bedtools to find overlapping lncRNAs in two files
# Find 100% overlapping genomic segments
bedtools intersect -a ./NONCODE/NONCODEv6_hg38.lncRNAGene.bed -b ./LncBook/lncRNA_gene_LncBookv2.0_GRCh38.bed -f 1 -r -s -wo > NONCODE_LncBook_overlapping_LncRNA.bed
# Extract the two IDs of successfully mapped lncRNAs from the overlapping file
awk -F'\t' '{print $4 "\t" $10}' NONCODE_LncBook_overlapping_LncRNA.bed > NONCODE_LncBook_Map.txt
# Merge files from both NONCODE and LncBook databases and remove duplicates
# Insert empty columns in both files, representing the ID from the other database
awk 'BEGIN {OFS="\t"} {print $1, $2, $3, $5, $6, $4, "-"}' ./NONCODE/NONCODEv6_hg38.lncRNAGene.bed > ./NONCODE/NONCODEv6_hg38.lncRNAGene_temp.bed
awk 'BEGIN {OFS="\t"} {print $1, $2, $3, $5, $6, "-", $4}' ./LncBook/lncRNA_gene_LncBookv2.0_GRCh38.bed > ./LncBook/lncRNA_gene_LncBookv2.0_GRCh38_temp.bed
echo "Please use merge.py to merge both files and remove duplicates"