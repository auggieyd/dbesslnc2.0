
// sql语句
var sqlMap = {
    property: {
      // 显示数据 
      //show final table data
      
      selectFinal: "select * from `final` ",
      //show essential lncRNA
      selectVital:"select * from `vital`",
      //show tumor suppressor genes
      selectTumor:"select * from `tumor`",
      //show essential lncRNA in cancer cell
      selectCancer:"select * from `cancer`",
      //show essential lncRNA in disease related
      selectDiseaseMap:
      "select * from `lncrna_variant_mapping` where UID = ?",
      //show essential lncRNA in disease related
      selectDisease:
      "select * from `variants` where variation_id IN (?)",

      //search page
      //organism is human
      selectHuman:
      "select * from `final` where Organism ='Human'",
       //organism is mouse
      selectMouse:
      "select * from `final` where Organism ='Mouse'",

      //reason is vital
      select_reason_vital:
      "select * from `final` where Role ='General'",
      //reason is tumor
      select_reason_tumor:
      "select * from `final` where Role ='Tumor suppressor gene'",
      //reason is cancer
      select_reason_cancer:
      "select * from `final` where Role ='Oncogene'",
      // cell growth
      select_cell_growth:
      "SELECT * FROM esslnc where role = 'Cell viability' limit ?,?",
      cell_count:
      "SELECT COUNT(*) AS total FROM esslnc where role = 'Cell viability'",
      disease_count:
      "SELECT COUNT(*) AS total FROM esslnc where disease_related = 1",
      // exp_crispr
      select_exp_crispr:
      "select * from `exp_crispr`",
      // diease related
      select_diease_related:
      "select * from esslnc where disease_related = 1 limit ?,?",


      //fuzzy search 模糊查询
      searchHuman:
      'select * from `esslnc` where Organism ="Human" AND concat(gene_name,Alias,Noncode_id,reason) like "%"?"%"',
      searchMouse:
      'select * from `esslnc` where Organism ="Mouse" AND concat(gene_name,Alias,Noncode_id,reason) like "%"?"%"',
      searchVital:
      'select * from `esslnc` where  concat(gene_name,Alias,Noncode_id,reason) like "%"?"%"',
      searchTumor:
      'select * from `esslnc` where  concat(gene_name,Alias,Noncode_id,reason) like "%"?"%"',
      searchCancer:
      'select * from `esslnc` where concat(gene_name,Alias,Noncode_id,reason) like "%"?"%"',
      searchCell:
      'select * from `esslnc` where role = "Cell viability" AND concat(gene_name,Alias,Lncbook_id,Noncode_id,reason) like "%"?"%"',
      searchDisease:
      'select * from `esslnc` where disease_related = 1 AND concat(gene_name,Alias,Lncbook_id,Noncode_id,Reason) like "%"?"%"',
      
      //用于模糊查询的输入建议
      fuzzyHuman:
      "select Name from `final` where Organism ='Human' order by Name",
      fuzzyMouse:
      "select Name from `final` where Organism ='Mouse' order by Name",
      fuzzyVital:
      "select DISTINCT gene_name from `esslnc` where vivo = 1 order by gene_name",
      fuzzyTumor:
      "select DISTINCT gene_name from `esslnc` where cancer_related = 2 order by gene_name",
      fuzzyCancer:
      "select DISTINCT gene_name from `esslnc` where cancer_related = 1 order by gene_name",
      fuzzyCell:
      "select DISTINCT gene_name from `esslnc` where role = 'Cell viability' AND gene_name != '-' order by gene_name",
      fuzzyDisease:
      "select DISTINCT gene_name from `esslnc` where disease_related = 1 AND gene_name != '-' order by gene_name",

      //用于blast页面 通过 转录本id 查找对应的内容
      // fuzzySeq:
      // 'select * from `trans` where NONCODE_TRANSCRIPT_ID in (?)',
      // "select * from `trans` where NONCODE_TRANSCRIPT_ID in ("?")"
      //用于 visual 页面 ，通过ID 查询对应的内容，做可视化
      profile:
      'select * from `exp_profile` where Lncbook_trans_id = ?',
      transcript:
      'select * from `trans` where UID = ?',
      gene:
      'select * from `esslnc` where UID = ?',
      experiment:
      'select * from `exp_crispr` where UID = ?',
    }
  };
  
  module.exports = sqlMap;
  