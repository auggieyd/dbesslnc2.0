echo "Convert the TXT file to a BED file and adjust the 1-based coordinates to 0-based coordinates."
awk -F'\t' 'NR > 1 {OFS="\t"; print $1, $2-1, $3, $4, $5, $6}' crispr.txt > crispr_lnc.bed

echo "Map Variants to LncRNAs"
bedtools intersect -a crispr_lnc.bed -b ../../variants/left-shift/variant_summary_GRCh38_filtered_left_shift_length.bed -wa -wb > crispr_variant_tmp.bed

echo "Cat header"
cat header.txt crispr_variant_tmp.bed > crispr_variant_complete.bed

rm crispr_variant_tmp.bed