#!/usr/bin/env bash
set -euo pipefail

# Usage: ./bed12_nonmmut_to_exons_csv.sh input.bed output.csv
# Input is a BED12 file.
# Output CSV columns:
# chrom,tx_start,tx_end,transcript_id,strand,exon_count,exons
# - tx_start: 1-based transcript start (= $2 + 1)
# - tx_end:   1-based transcript end (= $3)
# - exon_count: number of valid exons
# - exons: "exon1_start-exon1_end,exon2_start-exon2_end,..."

INPUT_FILE="./NONCODE/NONCODEv6_mm10.lncAndGene.bed"
OUTPUT_FILE="./NONCODE/NONCODEv6_lncRNA_trans_mouse.csv"

awk -v OFS="," '
BEGIN {
  # CSV header
  print "chrom","start","end","Noncode_trans_id","strand","exon_num","exon_pos";
}
$4 ~ /^NONMMUT/ {
  chrom = $1;
  tx_start = $2 + 1;
  tx_end   = $3;
  tid   = $4;
  strand = $6;

  cnt = ($10 + 0);
  split($11, bs, /,/);
  split($12, st, /,/);

  exons = "";
  exon_count = 0;
  for (i = 1; i <= cnt; i++) {
    if (bs[i] == "" || st[i] == "") continue;
    exon_start = $2 + st[i] + 1;
    exon_end   = $2 + st[i] + bs[i];
    exon_count++;
    if (exons != "") exons = exons ",";
    exons = exons exon_start "-" exon_end;
  }

  print chrom, tx_start, tx_end, tid, strand, exon_count, "\"" exons "\"";
}
' "$INPUT_FILE" > "$OUTPUT_FILE"

echo "Done. Wrote CSV to: $OUTPUT_FILE"
