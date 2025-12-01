<template>
  <div>
    <el-row 
      class="title" 
      type="flex" 
      justify="center" 
      align="middle" 
      style="color: #606060;"
    >
      <img
        src="../../public/assets/img/home.png"
        style="height: 45px; width:auto; vertical-align: middle; margin-right:10px;"
        alt="Home Icon"
      />
      Welcome to dbEssLnc2.0
    </el-row>

    <el-row :gutter="40" style="padding: 20px 0;">
      
      <el-col 
        :xs="24" 
        :sm="24" 
        :md="10" 
        :lg="10" 
        :xl="10" 
        :offset="2" 
        class="content-col"
      >
        <i class="el-icon-info duiqi-title">
          <em>&nbsp;Introduction of dbEssLnc2.0</em>
        </i>
        
        <p>
          <b>dbEssLnc2.0</b> is the abbreviation of <b>Ess</b>ential <b>Lnc</b>RNA
          database, version 2.0. 
        </p>
        
        <p>
          The
          <router-link to="/home"><b><i>Home</i></b></router-link>
          page mainly describes the organization of the dbEssLnc server.
        </p>
        <p>
          The
          <router-link to="/browse"><b><i>Browse</i></b></router-link>
          page categories all essential lncRNA.
        </p>
        <p>
          The
          <router-link to="/search"><b><i>Search</i></b></router-link>
          page provides the ability to search by the gene UID/name/aliases/NONCODE gene ID/LncBook gene ID/reason of essential lncRNA.
        </p>
        <p>
          The
          <router-link to="/blast"><b><i>Blast</i></b></router-link>
          page incorporates the Blast tool for comparing user-entered sequences 
          with those in the dbEssLnc2.0 database.
        </p>
        <p>
          The
          <router-link to="/download"><b><i>Download</i></b></router-link>
          page list all static links to the data packages and source code in the dbEssLnc2.0
          database.
        </p>
        <p>
          The
          <router-link to="/help"><b><i>Help</i></b></router-link>
          page provides three parts: the Tutorial part gives detailed instruction on how to use the dbEssLnc2.0 database, 
          the Statistics part shows the basic data analysis of the database according to organism and reason, 
          the Contact part provides information on how to contact authors of the database.
        </p>
        
        <p>
          Currently, <b>2716</b> essential lncRNA gene records are deposited in the 
          dbEssLnc2.0 database,and new data are constantly added by manual screening.
        </p>
        <p>
          Last update on: Jan.2th.2025.
        </p>
        
        <i class="el-icon-info duiqi-title citiation-title">
          <em>&nbsp;Citiation</em>
        </i>
        <p>1. Zhang Y Y, Zhang W Y, Xin X H, Du P F. dbEssLnc: A manually curated database of human and mouse essential lncRNA genes[J]. Computational and Structural Biotechnology Journal, 2022, 20: 2657-2663.
        </p>
        <p>2. Liu Y D, Gong X J, Du P F. dbEssLnc2.0: exploring disease-associated essential long noncoding RNAs in human cell lines[J]. Frontiers of Computer Science, (submitted).</p>
      </el-col>

      <el-col 
        :xs="24" 
        :sm="24" 
        :md="10" 
        :lg="10" 
        :xl="10" 
        class="content-col image-section"
      >
        <img
          alt="essential lncRNA"
          src="../../public/assets/img/home.svg"
          class="home-image"
        />
        
        <div class="workflow-description">
          <p>
            <b>The work flow of data curation process:</b><br/> 
            Work flow is divided to 4 steps. Step1: Using key words to collect essential 
            lncRNA data in PubMed. Step2: Manually extract the CRISPR experimental results for each lncRNA across different cell lines and map the variant sites in the ClinVar database to lncRNAs.
            Step3: Map genomic coordinates from hg19 to hg38 and map lncRNAs to other databases to retrieve additional details.
            Step4:Four categories of essential lncRNAs are deposited in the dbEssLnc2.0<br/> 
            <br>
            <b>Architecture of dbEssLnc2.0:</b><br/>
            dbEsslnc has seven functional pages, including "Browse", 
            "Search","Blast","Download","Help", "Gene" and "Visual" page. Users click the gene name in the "Browse" and "Search" 
            to jump to the "Gene" page for detailed information of gene. "Gene" page can jump to 
            "Visual" page to get information about lncRNA transcript by clicking gene transcript id .
          </p>
        </div>
      </el-col>
      
    </el-row>
  </div>
</template>

<script setup>

import { ElRow, ElCol } from 'element-plus';
</script>


<style scoped>

.title {
  height: 80px;
  font-size: 1.5em;

  display: flex; 
  align-items: center;
  justify-content: center;
  
  background: linear-gradient(135deg, #e6f0ef 45%, #b4ede7 100%); 
}


.content-col {
  padding: 0 10px;
}

.duiqi-title {
  display: block; 
  text-align: left;
  color: #606060; 
  margin: 50px 0 15px 0;
  font-size: 18px;
}

.citiation-title {
    margin-top: 18px; 
}


.content-col p {
  line-height: 200%;
  font-size: 16px;
  text-align: left; 
  margin: 10px 0; 
}


.home-image {
  width: 100%; 
  margin-top: 20px;
}


.workflow-description p {
    margin: 20px 0 0 0; 
    text-align: left; 
}


@media (max-width: 992px) {
  .image-section {
    margin-top: 30px; 
  }
}

</style>