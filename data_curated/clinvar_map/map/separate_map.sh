echo "Map Variants to NONCODE LncRNAs"
bedtools intersect -a ../lncRNA_reference/NONCODE/NONCODEv6_hg38.lncRNAGene.bed -b ../variants/left-shift/variant_summary_GRCh38_filtered_left_shift_length.bed -wa -wb > noncode_lncRNA_variant_tmp.bed

echo "Map Variants to LncBook LncRNAs"
bedtools intersect -a ../lncRNA_reference/LncBook/lncRNA_gene_LncBookv2.0_GRCh38.bed -b ../variants/left-shift/variant_summary_GRCh38_filtered_left_shift_length.bed -wa -wb > lncbook_lncRNA_variant_tmp.bed

echo "Cat header"
cat header.txt noncode_lncRNA_variant_tmp.bed > noncode_lncRNA_variant.bed
cat header.txt lncbook_lncRNA_variant_tmp.bed > lncbook_lncRNA_variant.bed

echo "Delete temp file"
rm noncode_lncRNA_variant_tmp.bed
rm lncbook_lncRNA_variant_tmp.bed
