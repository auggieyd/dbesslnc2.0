awk -F',' '$2 != "-" {print $2}' ../map/lncRNA.csv > lncbook_ids.txt
awk -F',' '$2 == "-" {print $1}' ../map/lncRNA.csv > noncode_ids.txt