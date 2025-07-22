echo "Map Variants to LncRNAs"
bedtools intersect -a ../lncRNA_reference/NONCODE_LncBook_same_merged.bed -b ../variants/left-shift/variant_summary_GRCh38_filtered_left_shift_length.bed -wa -wb > lncRNA_variant_tmp.bed

echo "Cat header"
cat header.txt lncRNA_variant_tmp.bed > lncRNA_variant_complete.bed
