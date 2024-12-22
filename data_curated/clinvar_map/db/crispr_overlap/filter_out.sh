#  convert crispr_lnc.csv&final_lncRNA.csv to bed file
awk -F, 'NR>1 {OFS="\t"; print $1, $2, $3, $4, $5, $6}' crispr_lnc.csv > crispr_lnc.bed

# use bedtools to find lncRNAs with an overlap rate of 1.
bedtools intersect -a final_lncRNA.bed -b crispr_lnc.bed -f 1 -r -s -wa -wb > overlapping_lncRNA.bed

# Delete completely overlapping lncRNAs
awk -F'\t' 'NR==FNR {key[$1 FS $2 FS $3]=1; next} !($1 FS $2 FS $3 in key)' overlapping_lncRNA.bed final_lncRNA.bed > final_lncRNA_nocrispr.bed
# Delete the corresponding mapping entries
awk -F'\t' 'NR==FNR {key[$4 FS $5]=1; next} !($7 FS $6 in key)' overlapping_lncRNA.bed ../../map/lncRNA_variant_complete.bed > lncRNA_variant_nocrispr.bed