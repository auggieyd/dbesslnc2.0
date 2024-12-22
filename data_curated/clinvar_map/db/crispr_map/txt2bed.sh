echo "Convert the TXT file to a BED file and adjust the 1-based coordinates to 0-based coordinates."
awk -F'\t' 'NR > 1 {OFS="\t"; print $1, $2-1, $3, $4, $5, $6}' crispr.txt > crispr_lnc.bed