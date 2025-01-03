# 
library(GeneSummary)
tb <- loadGeneSummary(organism = 9606)

gene_ids <- read.table("ncbi_gene_id.txt", header = FALSE, stringsAsFactors = FALSE)
colnames(gene_ids) <- c("Gene_ID") 

filtered_tb <- tb[tb$Gene_ID %in% gene_ids$Gene_ID, ]

go_map <- filtered_tb[, c("Gene_ID", "Gene_summary")]

write.table(go_map, file = "go_map.txt", sep = "\t", row.names = FALSE, quote = FALSE)
