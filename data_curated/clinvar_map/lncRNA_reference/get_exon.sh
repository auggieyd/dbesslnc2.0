# Extract transcripts for each gene, obtain mapping of gene ID and transcript ID
# For the lncbook's gtf, obtain the number of exons per transcript by counting

tac lncRNA_LncBookv2.0_GRCh38.gtf | awk -F '\t' '
$3 == "exon" {
    match($9, /transcript_id "[^"]+"/);
    transcript_id = (RSTART > 0 ? substr($9, RSTART+15, RLENGTH-16) : "");
    if (transcript_id != "") {
        exon_range = $4 "-" $5;
        if (!(transcript_id in exon_ranges)) {
            exon_ranges[transcript_id] = exon_range;
            exon_numbers[transcript_id] = 1;
        } else {
            exon_ranges[transcript_id] = exon_ranges[transcript_id] "," exon_range;
            exon_numbers[transcript_id]++; 
        }
    }
}
$3 == "transcript" {
    match($9, /gene_id "[^"]+"/);
    gene_id = (RSTART > 0 ? substr($9, RSTART+9, RLENGTH-10) : "");
    match($9, /transcript_id "[^"]+"/);
    transcript_id = (RSTART > 0 ? substr($9, RSTART+15, RLENGTH-16) : "");
    if (gene_id != "" && transcript_id != "") {
        exon_range = (transcript_id in exon_ranges ? "\"" exon_ranges[transcript_id] "\"" : "");
        exon_number = (transcript_id in exon_numbers ? exon_numbers[transcript_id] : "");
        print gene_id "," transcript_id "," $1 "," $4 "," $5 "," $7 "," exon_number "," exon_range;
    }
}' > LncBookv2.0_lncRNA_transcripts_temp.csv
tac LncBookv2.0_lncRNA_transcripts_temp.csv > LncBookv2.0_lncRNA_transcripts.csv
rm LncBookv2.0_lncRNA_transcripts_temp.csv

# NONCODE's gtf file contains exon_number directly, just extract it
tac NONCODEv6_human_hg38_lncRNA.gtf | awk -F '\t' '
$3 == "exon" {
    match($9, /transcript_id "[^"]+"/);
    transcript_id = (RSTART > 0 ? substr($9, RSTART+15, RLENGTH-16) : "");
    if (transcript_id != "") {
        exon_range = $4 "-" $5; 
        if (!(transcript_id in exon_ranges)) {
            exon_ranges[transcript_id] = exon_range; 
        } else {
            exon_ranges[transcript_id] = exon_ranges[transcript_id] "," exon_range;  
        }
    }
}
$3 == "transcript" {
    match($9, /gene_id "[^"]+"/);
    gene_id = (RSTART > 0 ? substr($9, RSTART+9, RLENGTH-10) : "");
    match($9, /transcript_id "[^"]+"/);
    transcript_id = (RSTART > 0 ? substr($9, RSTART+15, RLENGTH-16) : "");
    match($9, /exon_number [0-9]+/);
    exon_number = (RSTART > 0 ? substr($9, RSTART+12, RLENGTH-12) : "");
    if (gene_id != "" && transcript_id != "") {
        exon_range = (transcript_id in exon_ranges ? "\"" exon_ranges[transcript_id] "\"" : ""); 
        print gene_id "," transcript_id "," $1 "," $4 "," $5 "," $7 "," exon_number "," exon_range;
    }
}' > NONCODEv6_lncRNA_transcripts_temp.csv
tac NONCODEv6_lncRNA_transcripts_temp.csv > NONCODEv6_lncRNA_transcripts.csv
rm NONCODEv6_lncRNA_transcripts_temp.csv