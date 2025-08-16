// SQL statements
var sqlMap = {
    property: {
      // Display data
      //show final table data
      
      selectFinal: "select * from `final` ",
      //show essential lncRNA
      selectVital: "select * from `esslnc` where vivo = 1 order by UID ASC",  //show tumor suppressor genes
      selectTumor:"select * from `esslnc` where cancer_related = 2 order by UID ASC",
      //show essential lncRNA in cancer cell
      selectCancer:"select * from `esslnc` where cancer_related = 1 order by UID ASC",
      //show essential lncRNA in disease related
      selectDiseaseMap:
      "select * from `lncrna_variant_mapping` where UID = ?",
      //show essential lncRNA in disease related
      selectDisease:
      "select * from `variants` where variation_id IN (?)",

      //search page
      //organism is human
      selectHuman:
      "select * from `esslnc` where Organism ='Human' order by UID ASC limit ?,? ",  //organism is mouse
      selectMouse:
      "select * from `esslnc` where Organism ='Mouse' limit ?,?",

      //reason is vital
      select_reason_vital:
      "select * from `esslnc` where vivo = 1 order by UID ASC limit ?,?",
      //reason is tumor
      select_reason_tumor:
      "select * from `esslnc` where cancer_related = 1 order by UID ASC limit ?,?",
      //reason is cancer
      select_reason_cancer:
      "select * from `esslnc` where cancer_related = 2 order by UID ASC limit ?,?",
      // cell growth
      select_cell_growth:
      "SELECT * FROM esslnc where vitro = 1 order by UID ASC limit ?,?",
      cell_count:
      "SELECT COUNT(*) AS total FROM esslnc where vitro = 1",
      disease_count:
      "SELECT COUNT(*) AS total FROM esslnc where disease_related = 1",
      // exp_crispr
      select_exp_crispr:
      "select * from `exp_crispr`",
      // diease related
      select_diease_related:
      "select * from esslnc where disease_related = 1 order by UID ASC limit ?,? ",


      //fuzzy search 
      searchHuman:
      'select * from `esslnc` where Organism ="Human" AND concat(UID,gene_name,Alias,Noncode_id,Lncbook_id,reason_summary) like "%"?"%"',
      searchMouse:
      'select * from `esslnc` where Organism ="Mouse" AND concat(UID,gene_name,Alias,Noncode_id,Lncbook_id,reason_summary) like "%"?"%"',
      searchVital:
      'select * from `esslnc` where  concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason_summary) like "%"?"%"',
      searchTumor:
      'select * from `esslnc` where  concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason_summary) like "%"?"%"',
      searchCancer:
      'select * from `esslnc` where concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason_summary) like "%"?"%"',
      searchCell:
      'select * from `esslnc` where vitro = 1 AND concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason_summary) like "%"?"%"',
      searchDisease:
      'select * from `esslnc` where disease_related = 1 AND concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason_summary) like "%"?"%"',
      
      // For fuzzy search input suggestions
      fuzzyHuman:
      "select DISTINCT gene_name from `esslnc` where Organism ='Human' AND gene_name != 'N.A.' order by gene_name",
      fuzzyMouse:
      "select DISTINCT gene_name from `esslnc` where Organism ='Mouse' AND gene_name != '-' order by gene_name",
      fuzzyVital:
      "select DISTINCT gene_name from `esslnc` where vivo = 1 AND gene_name != '-' order by gene_name",
      fuzzyTumor:
      "select DISTINCT gene_name from `esslnc` where cancer_related = 2 AND gene_name != '-' order by gene_name",
      fuzzyCancer:
      "select DISTINCT gene_name from `esslnc` where cancer_related = 1 AND gene_name != '-' order by gene_name",
      fuzzyCell:
      "select DISTINCT gene_name from `esslnc` where vitro = 1 AND gene_name != 'N.A.' order by gene_name",
      fuzzyDisease:
      "select DISTINCT gene_name from `esslnc` where disease_related = 1 AND gene_name != '-' order by gene_name",

      // For BLAST page: query content by transcript ID
      // fuzzySeq:
      // 'select * from `trans` where NONCODE_TRANSCRIPT_ID in (?)',
      // "select * from `trans` where NONCODE_TRANSCRIPT_ID in ("?")"
      // For visualization page: query content by ID for visualization
      profileHuman:
      'select * from `exp_profile` where transcript_id = ? AND UID = ?',
      profileMouse:
      'select * from `expression` where transcript_id = ? AND UID = ?',
      transcript:
      'select * from `trans` where UID = ?',
      gene:
      'select * from `esslnc` where UID = ?',
      experiment:
      'select * from `exp_crispr` where UID = ?',
    }
  };
  
  module.exports = sqlMap;
