# Data Collection and Processing Process

## Essential lncRNA Verified by CRISPR Experiment

### 1. Download the data from the original literature and the genomic reference annotation file.

- CRISPR i  
  - Experimental and Analytical Results [Supplementary Table S4][https://www.science.org/action/downloadSupplement?doi=10.1126%2Fscience.aah7111&file=aah7111-tables3.xlsx] 
  - The reference genome annotation used in the study: genomic information(hg19)[ GTF](https://github.com/symbiologist/dualgenomewide/blob/main/analysis/reference/output/00_lncrna_reference/lncrna.gtf.gz)
- CRISPR delete
  - MAGeCK results of negatively and positively selected lncRNAs in Huh7.5 cell line.  [Supplementary Table 5](https://static-content.springer.com/esm/art%3A10.1038%2Fnbt.3715/MediaObjects/41587_2016_BFnbt3715_MOESM32_ESM.xlsx) 
  - MAGeCK results of negatively and positively selected lncRNAs in HeLa cell line. [Supplementary Table 9](https://static-content.springer.com/esm/art%3A10.1038%2Fnbt.3715/MediaObjects/41587_2016_BFnbt3715_MOESM36_ESM.xlsx)
  - The reference genome annotation used in the study:[GENCODEV19](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_19/gencode.v19.long_noncoding_RNAs.gtf.gz)
- CRISPR splice  
  - Screen scores of lncRNAs by splicing-targeting screen in multiple cell lines [Supplementary Table 6](https://static-content.springer.com/esm/art%3A10.1038%2Fnbt.4283/MediaObjects/41587_2018_BFnbt4283_MOESM23_ESM.xlsx)
  - The reference genome annotation used in the study: enomic information(hg38) [GENCODEV20]()
- CRISPR CasRx
  - Genomic annotation information and screen score information files used in the experiment. [Supplementary Table](https://static-content.springer.com/esm/art%3A10.1038%2Fs41592-024-02190-0/MediaObjects/41592_2024_2190_MOESM4_ESM.zip)
- LncRNA 
  - NONCODE V6 LncRNA and LncRNA Genes[ NONCODEv6_hg38.lncAndGene.bed.gz](http://www.noncode.org/datadownload/NONCODEv6_hg38.lncAndGene.bed.gz);[ NONCODEv6_human.fa.gz](http://www.noncode.org/datadownload/NONCODEv6_human.fa.gz)
  - LncBook V2.0[ lncRNA_LncBookv2.0_GRCh38.gtf.gz](https://ngdc.cncb.ac.cn/lncbook/files/lncRNA_LncBookv2.0_GRCh38.gtf.gz); [ lncRNA_LncBookv2.0.fa.gz](https://ngdc.cncb.ac.cn/lncbook/files/lncRNA_LncBookv2.0.fa.gz)
  - GENCODE V47[gencode.v47.long_noncoding_RNAs.gtf](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_47/gencode.v47.long_noncoding_RNAs.gtf.gz)
  - HGNC[non-coding_RNA.txt]( https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/locus_groups/non-coding_RNA.txt)

### 2. Essential long non-coding RNA gene screening and filtering

Different studies use various methods to measure the impact of lncRNAs on cell viability, and we need to filter based on the settings established in each study.

- **CRISPR i  :**  Extracting information from the table involves filtering different cell lines according to the columns. The criteria for retention are that the `lncRNA gene hit type`columns value must be `lncRNA hit` and the `screen score` columns value must greater than 7  and the `ave_Rep1_Rep2|average phenotype of strongest 3 sgRNAs)`column value must be less than 0. It is important to note that for the IPSC cell line, the selection is `gamma_T0vT12`.

  ![image-20241217142938151](./assets/image-20241217142938151.png)

- **CRISPR delete:** To extract essential non-coding lncRNAs from the table,follow these three criteria: 1)Select only the tables that indicate `Negative selection`; 2)Retain rows where the`neg|fdr`column has values less than 0.25; 3)Remove rows that correspond to coding genes.

  ![image-20241217143411763](./assets/image-20241217143411763.png)

- **CRISPR splice :** To extract necessary non-coding lncRNAs from the table,apply the following criteria: 

  1)Retain rows where the`Gene_symbol`column indicates non-coding RNAs; 

  2)Keep only those rows where the`Screen_score`column has values greater than **2**.

  ![image-20241217144213740](./assets/image-20241217144213740.png)

- **CRISPR CasRx :** In the "Supplementary_table12.csv" file, the relevant analysis information for this study is stored. We extract the table information based on the `dropFDR` column value being less than 0.25 and the `library` column being "ALBAROSSA_library" for a specific cell line. Here, only one cell line is displayed.

![image-20241217145322449](./assets/image-20241217145322449.png)

- **Result** In the aforementioned study, all essential long non-coding RNA entries of interest, including their identifiers from experiments (custom gene IDs or public database gene names), cell lines,  experimental scores and PUBMED ID have been manually recorded in `/curated/exp_crispr.csv`.  

![image-20241218151707479](./assets/image-20241218151707479.png)

Due to differences in eras and annotation discrepancies, we need to further update and supplement the annotations to construct a high-quality, usable dataset. 

### 3. Annotations Updates and Complements

#### Genome Coordinate Alignment

1. Store the extracted lncRNA identifiers as a list in the first step. Extract the annotation information corresponding to the reference genome.

   Details see code: `/match/coor_match.ipynb:step1` 

   > Only for`crispr_splice`and`crispr_delete`. After executing the aforementioned code, adjust the code to generate   crispr_xxxx_seq.bed  . If it's the hg19 version, further operations are required to convert to hg38.
   
   ```python
   id_field = extract_attribute(attributes, 'exon_id') 
   #-->
   id_field = extract_attribute(attributes, 'transcript_id')
   ```
   
   > noted that : The supplementary data of the (CRISPR casRx) literature provides the reference coordinates for the hg38 genome.

#### Genome Coordinate convert

Using the LiftOver tool to convert the hg19 version to hg38.

```
# Download the Liftover tool.
wget http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/liftOver
# Download the chain file.
wget http://hgdownload.soe.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz
```

Prepare the input BED file ,`crispri.bed`and`crispr_delete.bed`

Run LiftOver e.g.

```
./liftOver crispri/crispri18.bed hg19ToHg38.over.chain.gz crispri38.bed unmapped.bed
```

`unmapped.bed`: Contains unmapped regions with reasons for failure.  Those that fail to convert require further manual inspection and processing.

#### Merge lncRNA entries

1. The merging criterion is based on the lowest exon-level coordinate range to combine lncRNA entries from four different literature sources; if two genes contain at least one transcript in common and on the same strand., they are considered the same gene.

```
bedtools intersect -a crispr_delete38.bed -b crispr_splice38.bed -wo -s -r -f 1 > temp.bed
# For genes with individual exons that are 100% overlapping in the results processed by bedtools, manual checks are
# conducted. Sequence region annotations updates caused by updates to public databases, 
# such as (GENCODE), are also merged into the same entry.
# For example: RP11-540O11.1-RP11-540O11.1, TMEM9B-AS1-LH02375, etc.
```

Detailed data processing. Details see code: `/match/coor_match.ipynb:step3`. Conduct manual checks on the exons reported in tocheck.txt that have 100% overlap.

2. Generate a merge.txt file. The complete merge process can be seen in the code:`/match/coor_match.ipynb:step4`

   ![image-20241217233557071](./assets/image-20241217233557071.png)

#### Map the coordinate ranges to th latest public database to obtain annotations

Obtain gene IDs from the NONCODE V6 , LncBook,and GENCODE databases to enhance data usability.

1. Convert GTF files into custom BED files for ease of subsequent filtering.
2. Based on the complete matching of lowest exon-level coordinate ranges and on the same strand., if a gene matches multiple genes, select the one with the largest overlapping range.

```
 bedtools intersect -a crispr_all.bed -b lncbook.bed -wo -s -r -f 1 > lctemp.bed
 bedtools intersect -a crispr_all.bed -b noncode.bed -wo -s -r -f 1 > nctemp.bed
 bedtools intersect -a crispr_all.bed -b gencodev47.bed -wo -s -r -f 1 > gctemp.bed
```

3. Generate database annotations **mapping files**. See the detailed selection code at`/match/map_annotations.ipynb`

   **mapping files**:`lncbook_map.tsv,noncode_map.tsv,gencode_map.tsv`

4. Obtaining NCBI Gene IDs by matching th`gene_name`field in th`gencode_map.ts`file with the symbol field in the `non-coding_RNA.txt` file downloaded from HGNC.

#### Map the  Ontology Annotations 

1. Obtaining NCBI Gene IDs by matching th`gene_name`field in th`gencode_map.tsv`file with the symbol field in th`non-coding_RNA.txt`file downloaded from HGNC.

   Details see code: `/match/map_annotations.ipynb`

2. Use the `GeneSummary` R package to obtain Gene Ontology annotations via NCBI gene ID.

   - Install `GeneSummary` R package in R 4.3.3

   ```R
   if (!require("BiocManager", quietly = TRUE))
       install.packages("BiocManager")
   
   BiocManager::install("GeneSummary")
   ```

   - Execute the script file.`/match/map_go.R`

#### To obtain sequence 

1. Using the REST API provided by Ensembl to obtain the sequence of a gene region.`/match/get_seq.py`

   ```python
   python get_seq.py
   ```

2. Based on public lncRNA databases such as NONCODE that store exon-level sequences, splice the sequences from previous step and generate a FASTA file.

   > Before this step,you need to modify the content of`coor_match.ipynb`step1,specifically for the Gencode GTF file.
   > `id_field = extract_attribute(attributes, 'exon_id') -->id_field = extract_attribute(attributes, 'transcript_id')`
   > See the code.`/match/gen_fa.ipynb`



## Putative Essential lncRNA Based on Pathogenic Variant Data from the ClinVar Database

### 1. Download the data from the public database and the genomic reference annotation file.

- Variants
  - Tab-delimited report for variants  which have been submitted to ClinVar[variant_summary.txt.gz](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz)
  - VCF file of variants with precise endpoints [clinvar_20240603.vcf.gz](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar_20241215.vcf.gz)
  - XML file with variant length [ClinVarVCVRelease_2024-09.xml.gz](https://ftp.ncbi.nlm.nih.gov/pub/clinvar/xml/ClinVarVCVRelease_2024-09.xml.gz)
- LncRNA 
  - NONCODE V6 LncRNA and LncRNA Genes[ NONCODEv6_hg38.lncAndGene.bed.gz](http://www.noncode.org/datadownload/NONCODEv6_hg38.lncAndGene.bed.gz)
  - LncBook V2.0[ lncRNA_LncBookv2.0_GRCh38.gtf.gz](https://ngdc.cncb.ac.cn/lncbook/files/lncRNA_LncBookv2.0_GRCh38.gtf.gz)
  - The hg38 coordinate file(1 base) of lncRNAs that have been validated by CRISPR,from`/store/dbess.ipynb:Step2.1`.
    `/store/crispr.txt`

### 2. Variants filtering and putative essential long non-coding RNA gene labelling.

#### Variants filtering 

1. Filter variants in `variant_summary.txt`. Firstly, the `Assembly` field should be `GRCh38`. Secondly, retain variants with at least one star and without conflicts. Finally, filter out variants that do not appear in the `clinvar_20240603.vcf` file. (Script: `/clinvar_map/variants/left-shift/pre_process.py`)
2. Obtain the variant length from `ClinVarVCVRelease_2024-09.xml`. (Script: `/clinvar_map/variants/left-shift/get_length_xml.py`)
3. Filter out variants longer than 100bp and calculate the left-shift coordinates for the variants. (Script: `/clinvar_map/variants/left-shift/after_process.py`)

#### Merge reference lncRNAs

1. Merge lncRNAs from NONCODEv6 and LncBookv2.0

   - Use `bedtools` to identify lncRNAs that have the same coordinate. (Script: `/clinvar_map/lncRNA_reference/merge_noncode_lncbook.sh`)

2. Merge lncRNAs from the two databases, retaining only one record for lncRNAs with same coordinate. (Script: `/clinvar_map/lncRNA_reference/merge.py`)

#### Map variants to reference lncRNAs set

1. Map variants to reference lncRNA set using `bedtools`. (Script: `/clinvar_map/lncRNA_reference/map.sh`)

2. Map result statistics (Script: `/clinvar_map/db/statistic/statistic.py`)

   - Retain mapping entries that include variants with clinical significance marked as `pathogenic` or `likely pathogenic`.

   - Count putative essential lncRNAs that overlap with pathogenic or likely pathogenic variants.(`/clinvar_map/db/statictis/lncRNA.csv`)

3. Annotate additional annotations for lncRNAs

   - Extact `Noncode ID` and `Lncbook ID` for ID conversion.(Script:`/clinvar_map/db/conversion/get_id_for_conversion.sh`)
   - Use the LncBook [**ID Conversion Tool** ](https://ngdc.cncb.ac.cn/lncbook/tools/conversion)to query the `NCBI_ID` and `gene_name` for lncRNAs. (Script: `/clinvar_map/db/conversion/id_conversion.py`) Generate:`/clinvar_map/db/conversion/lnbook_conversion_results.csv`and`/clinvar_map/db/conversion/noncode_conversion_results.csv`

   -  Merge`/clinvar_map/db/statistic/lncRNAs`, `/clinvar_map/db/conversion/lnbook_conversion_results.csv` and`/clinvar_map/db/conversion/noncode_conversion_results.csv`. (Script: `/clinvar_map/db/conversion/merge_NCBI_symbol.py`)

4. Filter out putative essential lncRNAs that have CRISPR experimental evidence(`/store/crispr.txt`). If a putative essential lncRNA has exactly the same coordinates as another essential lncRNA with experimental evidence, the putative essential lncRNA is deleted. Delete mappings associated with these putative essential.(Script:`/clinvar_map/crispr_overlap/filter_out.sh`)

5. Count pathogenic or likely pathogenic variants map to putative essential that don't have CRISPR experimental evidence. Count the mappings between pathogenic or likely pathogenic variants and putative essential lncRNAs. (Script:`/clinvar_map/criepr_overlap/statistic.py`) Generate:`/clinvar_map/db/crispr_overlap/variants_nocrispr.csv` and `/clinvar_map/db/crispr_overlap/lncRNA_variant_mapping_nocrispr.csv`

#### Map variants to  essential lncRNAs verified by CRISPR experiments.

1. Convert the txt file of essential lncRNAs verified by CRISPR experiments(`/store/crispr.txt `generated in`/store/dbess.ipynb:Step2.2 Export data for variants mapping`) to bed file.(Script:`/clinvar_map/db/crispr_map/txt2bed.sh`)

2. Map variants to lncRNAs using `bedtools`.(Scripts:`/clinvar_map/crispr_map/map.sh`)

3. Result statistics (Script: `/clinvar_map/db/crispr_map/statistic.py`)

   - Retain mapping entries that include variants with clinical significance marked as `pathogenic` or `likely pathogenic`.

   - Count experimentally verified essential lncRNAs that overlap with pathogenic or likely pathogenic variants.
     Generate： `/clinvar_map/db/crispr_map/crispr_lncRNA.csv`

   - Count pathogenic or likely pathogenic variants overlapped with experimentally verified essential lncRNAs.
     Generate：`/clinvar_map/db/crispr_map/crispr_variants.csv`

   - Organize the mapping relationship between variants and lncRNAs.
     Generate：`/clinvar_map/db/crispr_map/crispr_variants.csv`

## Sorting out the essential lncRNAs obtained through literature mining

A total of 172 cancer-related essential lncRNAs were manually collected.(`/cancer/cancer.txt`)

Generate a mapping file between `gene_name` and `gene_id` through`/match/map_annotations.ipynb:step1.1:Generate files for subsequent step`: `/match/gene_mapping.txt`.Based on this file,use `gene_name` as the key to obtain `gene_id`, and according to `gene_id`, retrieve annotation information from`/clinvar_map/lncRNA_redference/NONCODE_LncBook_same_merged.bed`. For lncRNAs that fail to map, obtain the information again using `Noncode_id`. (Script: `cancer/proCancerRelated.py`)

For the remaining seven lncRNAs that could not have their coordinate information retrieved from the reference lncRNA collection, manually search and supplement annotation information in the NCBI database.`/cancer/unmap_from_dbesslnc.txt`

<img src="./assets/image-20241222154012793.png" alt="image-20241222154012793" style="zoom:80%;" />

## Data management and storage into the database.

Using MySQL 8.0.40 for storing and managing databases.

For the database schema, please refer to the file   `/store/dbess_schema.sql`  .

1. Import the table structure file.

   ```
   mysql -u username -p
   USE database_name;
   SOURCE /path/to/your/dbess_schema.sql;
   ```

   ![image-20241220183835620](./assets/image-20241220183835620.png)

2. Import the lncRNA gene into the **esslnc** table. Execute the data import code `/store/dbess.ipynb：Step2,3` When importing data,simply modify the corresponding file names,table names,and field names, 

   - **Step2:Import gene entries**:Import genomic annotation information of lncRNA genes from three data sources.
     details see code:`/store/dbess.ipynb：Step2`
   - **Step3: Import the mapped gene IDs(for lncRNA verified by CRISPR  )**
     import the mapped public database gene IDs and gene names,along with other mapped data
     details see code:`/store/dbess.ipynb：Step3`

   > During the genome version conversion process, genes that fail to convert are manually checked and entered into the database.

3. Generate unique identifiers for human lncRNA to facilitate system management.Assign unique identifiers to the collected lncRNA genes following the allocation principle:`ELH+xxxxxx`,for example,`ELH000001`. 
   details see code:`/store/dbess.ipynb：Step4`

4. Import transcript annotations into the **trans** table (lncRNA verified by CRISPR). 

   - Using the UID from the previous step,generated by`dbess.ipynb:Step4.2`,the`seq_xxx.bed`generated by`/match/gen_fa.ipynb`,and the`/match/lncRNA2.fasta` file,generate basic annotations for transcripts and import them into the database.
   - Map public database IDs using `lncbook_map.tsv` and `noncode_map.tsv`.
   - For detailed code,see`/store/dbess.ipynb:Step5,6`.

5. Import transcript annotations into the **trans** table(lncRNA non verified by CRISPR)

   - Using the UID from the previous step,generated by`dbess.ipynb:Step4.5`,`non_crispr_UID.txt`
   - Extract the basic annotation information of these lncRNAs and import it into the database.Count the number of exons and record the coordinate for all reference lncRNA transcripts. (Script: `/clinvar_map/lncRNA_reference/get_exon.sh`).Retrieve the number and the coordinate of exon for  transcripts of all essential lncRNA genes. (Script: `/clinvar_map/db/exon/getExon.py`)
     Generate:`/clinvar_map/db/exon/non_crispr_lncRNA.csv`
   - Extract sequences from NONCODE and LncBook databases and import them into the database.
   - details see code:`/store/dbess.ipynb:step5.2,step5.3`

6. Import CRISPR experiment record`exp_crispr.csv` into **exp_crispr** table.

   - Details see code:`/store/dbess.ipynb:Step7`
   - Group by  exp_type  and  target_id  columns, for groups with a count of 1, mark as 'cell-line specific' and update in the table; for groups with a count of 2-5, mark as 'common essential'; and for groups with a count greater than 5, mark as 'core essential'.Details see code:`/store/dbess.ipynb:Step7.1`

7. Import variants Mapping file into **lncrna_variant_mapping ** table and variants file into the **variants** table

   - Create a local mapping table for lncRNA verified by crispr through `/store/dbess.ipynb: Step4.3` 
     Generate:`/store/crispr_UID.txt`. 
   - Create a local mapping table for disease_related lncRNAs through `/store/dbess.ipynb: Step4.4` 
     Generate:`/store/disease_related_UID.txt`. 
   - Replace `target` in `/clinvar_map/db/crispr_map/crispr_mapping.csv` with  `UID`    (Script:   `/clinvar_map/db/construct_map/get_map_crispr.py`  ).
     Generate:`/clinvar_map/db/construct_map/crispr_mapping.csv`
   - Replace `Noncode_id` and` Lncbook_id` in `/clinvar_map/db/crispr_overlap/lncRNA_variant_mapping_nocrispr.csv` with  `UID`    (Script:   `/clinvar_map/db/construct_map/get_map_disease.py`  ).
     Generate:`/clinvar_map/db/construct_map/disease_mapping.csv`
   - Import the table generated above.For detailed code,see`/store/dbess.ipynb:Step8`.

8. Import human lncRNA esspression file into **exp_profile** table

   - Create a local mapping table for  transcrispt `trans.txt`
   - Download the expression profile file for lncRNAs from LncExpDB: [expression_profiles_HPA.tar.gz](ftp://download.big.ac.cn/lncexpdb/1-NormalTissuesAndCellLines/1-TheHumanProteinAtlas/expression_profiles_HPA.tar.gz "size: 694.28M, last update: 2020-08-13") .
   - Calculate the mean TPM (Transcripts Per Million) of lncRNAs across different tissues. (Script: `/clinvar_map/db/exp/cal_exp.py`)
   - Retrieve the expression profile of lncRNAs. (Script: `/clinvar_map/db/exp/get_exp.py`
   - Import the table generated above.For detailed code,see`/store/dbess.ipynb:Step9`.
