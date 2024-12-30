<template>
  <div>
    <el-row class="title" style="color: #606060;">
      <img
        src="../../public/assets/img/home.png"
        style="height: 45px; width:auto;vertical-align: middle; margin-right:10px; margin-bottom:5px;"
      />
      Welcome to dbEssLnc2.0
    </el-row>
    <el-row :gutter="100" >
      <div class="wrapper">
        <el-col :span="2">

        </el-col>
        <el-col :span="10"  class="duiqi" >
          <i style="font-size: 20px;  color: #606060; margin: 40px 0 20px 0;" class="el-icon-info" >
            Introduction of dbEssLnc2.0</i>
          <!-- <p class="nav1">
            To visit dbEssLnc V1.0,<a href="https://esslnc.pufengdu.org/v1/" style="color: #551A8B;" target="_blank"> click here</a>
          </p> -->
          <p>
            <b>dbEssLnc2.0</b> is the abbreviation of <b>Ess</b>ential <b>Lnc</b>RNA
            database, version 2.0. 
          </p>
          <p>
            The
            <router-link to="/home"
              ><b><i>Home</i></b></router-link
            >
            page mainly describes the organization of the dbEssLnc server.
          </p>
          <p>
            The
            <router-link to="/browse"
              ><b><i>Browse</i></b></router-link
            >
            page categories all essential lncRNA.
          </p>
          <p>
            The
            <router-link to="/search"
              ><b><i>Search</i></b></router-link
            >
            page provides the ability to search by the gene UID/name/aliases/NONCODE gene ID/LncBook gene ID/reason of essential lncRNA.
           
          </p>
          <p>
            The
            <router-link to="/blast"
              ><b><i>Blast</i></b></router-link
            >
            page incorporates the Blast tool for comparing user-entered sequences 
            with those in the dbEssLnc2.0 database.
          </p>
          <p>
            The
            <router-link to="/download"
              ><b><i>Download</i></b></router-link
            >
            page list all static links to the data packages and source code in the dbEssLnc2.0
            database.
          </p>
          <p>
            The
            <router-link to="/help"
              ><b><i>Help</i></b></router-link
            >
            page provides three parts: the Tutorial part gives detailed instruction on how to use the dbEssLnc2.0 database, 
            the Statistics part shows the basic data analysis of the database according to organism and reason, 
            the Contact part provides information on how to contact authors of the database.
          </p>
          <p>
            Currently, <b>6315</b> essential lncRNAs are deposited in the
            dbEssLnc2.0 database,and new data are constently added by manual screening.
          </p>
          <p>
            Last update on: Nov.30th.2024.
          </p>
        </el-col>
        <el-col :span="10">
          <img
            alt="essential lncRNA"
            src="../../public/assets/img/framework.svg"
            style="width: 600px; margin-top: 90px;"
            
          />
          <div>
            <span style="font-size: 14px; float:right;" class="duiqi">
              <b></b>
              <p>The work flow of data curation process:<br/> 
                  Work flow is divided to 4 steps. Step1: Using key words to collect essential 
                  lncRNA data in PubMed. Step2: Manually extract the CRISPR experimental results for each lncRNA across different cell lines and map the variant sites in the ClinVar database to lncRNAs.
                   Step3: Map genomic coordinates from hg19 to hg38 and map lncRNAs to other databases to retrieve additional details.
                   Step4:Four categories of essential lncRNAs are deposited in the dbEssLnc2.0<br/>  
                  Architecture of dbEssLnc2.0:<br/>
                   dbEsslnc has seven functional pages, including "Browse", 
                    "Search","Blast","Download","Help", "Gene" and "Visual" page. Users click the gene name in the "Browse" and "Search" 
                    to jump to the "Gene" page for detailed information of gene. "Gene" page can jump to 
                    "Visual" page to get information about lncRNA transcript by clicking gene transcript id .
              </p>
               
            </span>
          </div>
        </el-col >
        <el-col :span="2">

        </el-col>
      </div>

    </el-row>
  </div>
</template>

<script>

</script>


<style scoped>
.title {
  text-align: center;
  font-size: 1.5em;
  line-height: 80px;
  justify-content: center;
  align-items: center;
  height: 80px;
  background: #e6f0ef; 
  background: -moz-linear-gradient(
    -45deg,
    #e6f0ef 45%,
    #b4ede7 100%
  ); 
  
  background: -webkit-linear-gradient(
    -45deg,
    #e6f0ef 45%,
    #b4ede7 100%
  ); /* Chrome10-25,Safari5.1-6 */
  background: linear-gradient(
    135deg,
    #e6f0ef 45%,
    #b4ede7 100%
  ); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#e6f0ef', endColorstr='#b4ede7',GradientType=1 ); /* IE6-9 fallback on horizontal gradient */
}
.duiqi{
  text-align: justify; 
 
}
.wrapper{
  display:flex;
  align-item:center;
  padding-left:10px;
}
.wrapper p{
  line-height:200%;
  font-size:16px;
}
.nav1{
  font-size: 18px;
  font-weight: bold;
  color: #606060;
  margin-top: 20px;
  margin-bottom: 20px;
  background-color: #f0f0f0; /* 浅灰色背景 */
  border-radius: 5px; /* 圆角边框 */
  padding: 5px;
}
</style>
