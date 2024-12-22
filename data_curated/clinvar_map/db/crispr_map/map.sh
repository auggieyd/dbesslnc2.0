
echo "Map Variants to LncRNAs"
bedtools intersect -a crispr_lnc.bed -b ../../variants/left-shift/variant_summary_GRCh38_filtered_left_shift_length.bed -wa -wb > crispr_variant_tmp.bed

echo "Cat header"
cat header.txt crispr_variant_tmp.bed > crispr_variant_complete.bed

rm crispr_variant_tmp.bed