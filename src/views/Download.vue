<template>
  <div>
    <el-row class="title" style="color: #606060;">
      <img
        src="../../public/assets/img/download.png"
        style="height: 45px; width: auto;  vertical-align: middle; margin-right: 20px;"
      />
      Download files
    </el-row>

    <div class="files">
      <h3>Download Data</h3>
      <div class="download-content" style="height:40%">
        <p>
          <img src="../../public/assets/img/downicon.png" class="icon" />
          <a :href="'/data/esslnc.xlsx'" download="">
            All essential lncRNA.xlsx
          </a>
          : This file contains all data.
        </p>
         <p>
          <img src="../../public/assets/img/downicon.png" class="icon" />
          <a :href="'/data/exp_crispr_records.xlsx'" download="">
            CRISPR Experimental Record.xlsx
          </a>
          : This file contains all CRISPR Experimental Record.
        </p>

        <p>
          <img src="../../public/assets/img/downicon.png" class="icon" />
          <a :href="'/data/disease_related.xlsx'" download="">
            Disease Related.xlsx
          </a>
          : This file contains all disease related  data.
        </p>
      </div>
    </div>
    <div class="files">
      <h3>dbEssLnc Scoure Codes</h3>
      <div class="download-content" style="height:40%">
        <div >
          <img src="../../public/assets/img/github.png" class="icon" />
          <a href=" https://github.com/auggieyd/dbesslnc2.0" target="_blank">
            https://github.com/auggieyd/dbesslnc2.0
          </a>
        </div>

     
          
         
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {

    };
  }
};
</script>

<style scoped>
.title {
  /* text-align: center; */
  font-size: 1.5em;
  line-height: 80px;
  height: 80px;
  justify-content: center;
  align-items: center;
  background: #e6f0ef; /* Old browsers */
  background: -moz-linear-gradient(
    -45deg,
    #e6f0ef 45%,
    #b4ede7 100%
  ); /* FF3.6-15 */
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

.download-content {
  display: flex;
  flex-direction: column;
  text-align: left;
  padding: 20px;
  border: 1px solid rgb(115, 200, 200);
  border-radius: 10px;
}
/* 
a {
  color: #232324;
} */

h3 {
  text-align: left;
  padding: 10px;
  background-color: rgb(115, 200, 200);
  color: #e6f0ef;
  border-radius: 10px;
}

.files {
  width: 70%;
  margin: 0 auto;
}

p {
  text-align: justify;
  line-height: 1.5em;
}

.icon {
  height: 1.5em;
  width: auto;
  vertical-align: middle;
  margin-right: 5px;
}
</style>
