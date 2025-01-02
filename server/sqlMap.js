
// sql语句
var sqlMap = {
    property: {
      // 显示数据 
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
      "select * from `esslnc` where vivo = 1 limit ?,?",
      //reason is tumor
      select_reason_tumor:
      "select * from `esslnc` where cancer_related = 1 limit ?,?",
      //reason is cancer
      select_reason_cancer:
      "select * from `esslnc` where cancer_related = 2 limit ?,?",
      // cell growth
      select_cell_growth:
      "SELECT * FROM esslnc where vitro = 1 limit ?,?",
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


      //fuzzy search 模糊查询
      searchHuman:
      'select * from `esslnc` where Organism ="Human" AND concat(UID,gene_name,Alias,Noncode_id,Lncbook_id,reason) like "%"?"%"',
      searchMouse:
      'select * from `esslnc` where Organism ="Mouse" AND concat(UID,gene_name,Alias,Noncode_id,Lncbook_id,reason) like "%"?"%"',
      searchVital:
      'select * from `esslnc` where  concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason) like "%"?"%"',
      searchTumor:
      'select * from `esslnc` where  concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason) like "%"?"%"',
      searchCancer:
      'select * from `esslnc` where concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason) like "%"?"%"',
      searchCell:
      'select * from `esslnc` where vitro = 1 AND concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,reason) like "%"?"%"',
      searchDisease:
      'select * from `esslnc` where disease_related = 1 AND concat(UID,gene_name,Alias,Lncbook_id,Noncode_id,Reason) like "%"?"%"',
      
      //用于模糊查询的输入建议
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

      //用于blast页面 通过 转录本id 查找对应的内容
      // fuzzySeq:
      // 'select * from `trans` where NONCODE_TRANSCRIPT_ID in (?)',
      // "select * from `trans` where NONCODE_TRANSCRIPT_ID in ("?")"
      //用于 visual 页面 ，通过ID 查询对应的内容，做可视化
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
  