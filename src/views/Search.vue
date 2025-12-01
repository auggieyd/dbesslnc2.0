<template>
    <div class="result">
        <div class="header">
          <el-row class="title" >
          <img
            src="../../public/assets/img/search.png"
              style="height: 45px; width: auto;  vertical-align: middle; margin-right: 20px;"
          />
          Search from Database
          </el-row>
          
          <el-autocomplete 
            placeholder="Search By Gene Name/Gene UID/Alias/NONCODE GENE ID/LncBook Gene ID/Detailed Reason Description,eg.Meg3/2900016C05Rik/NONMMUG009962.3/lethality" 
            v-model="inputContent" 
            clearable 
            @keyup.enter="Search" 
            class="input-with-select" 
            :fetch-suggestions="querySearch">
            <template #prepend >
              <el-select v-model="searchOpt" clearable placeholder="Human" class="select" >
                <el-option-group v-for="group in options"  :key="group.label" :label="group.label">
                  <el-option  v-for="item in group.options" :key="item.value" :label="item.label" :value="item.value">
                  </el-option>
                </el-option-group>
              </el-select>
            </template>

            <template #append>
              <el-button icon="el-icon-search" @click="Search"></el-button>
            </template>
            
          </el-autocomplete>
        </div>
        <div class="content" >
          <el-row v-if="id==0" style="padding: 5px;" class="content">
            <div class="wrapper">
              <el-col :span="12"  class="explain">
                <picture>
                  <source :srcset="require('@/assets/img/sta.webp')" type="image/webp">
                  <img :src="require('@/assets/img/sta.png')" alt="Search statistics and help" style="height: auto; width: 100%;">
                </picture>
              </el-col>
              <el-col :span="12" class="explain">
                <p>
                You can obtain the desired information by selecting the search type and searching for
                the corresponding name.If you want to know which are the essential lncRNAs in a certain
                type,you can directly select the type and click search.If you forget how to spell it,
                a fuzzy search can be performed by "%".More detailed fuzzy query rules are given in 'Search help'
                in the tutorial section of the 'Help' page.
                </p>
                <picture>
                  <source :srcset="require('@/assets/img/sea2.webp')" type="image/webp">
                  <img :src="require('@/assets/img/sea2.png')" alt="Search statistics and help" style="height: auto; width: 100%;">
                </picture>
              </el-col>
            </div>


          </el-row>
          
          <div class="tabletitle" v-if="id==1">
            <el-row>
              <el-col :span="4" :offset="10">
                Search results
              </el-col>
            </el-row>
          </div>
          <el-table
            v-if="id==1"
            
            :header-cell-style="{background:'#eef1f6',color:'#606266'}"
            :data="lncrnaTable"
            :row-class-name="tabRowClassName"
            empty-text="No data available"
            border
            style="width: 100%"
            ref="table"
          >
            <el-table-column label="Gene UID" prop="UID" width="110px" >
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>

            <el-table-column label="Symbol" prop="gene_name"  >
            </el-table-column>
            <el-table-column label="NCBI Gene ID" prop="NCBI_id"  width="120px">
              <template #default="scope">
                <span @click="toUrl_NCBI(scope.row.NCBI_id)" class="hand">{{scope.row.NCBI_id}}</span>
              </template>
            </el-table-column>
            <el-table-column label="LncBook Gene ID" prop="Lncbook_id"  width="150px">
              <template #default="scope">
                <span @click="toUrl_LncBook(scope.row.Lncbook_id)" class="hand">{{scope.row.Lncbook_id }}</span>
              </template>
            </el-table-column>
            <el-table-column label="NONCODE Gene ID" prop="NONCODEId"  width="170px">
              <template #default="scope">
                <span @click="toUrl_NONCODE(scope.row.Noncode_id)" class="hand">{{scope.row.Noncode_id }}</span>
              </template>
            </el-table-column>
            
            <el-table-column label="Organism" prop="Organism"  >
            </el-table-column>


            <el-table-column label="PubMedID" prop="PMID"  >
              <template #default="scope">
                <a :href="url+scope.row.PMID" target="_black">
                  {{scope.row.PMID}}
                </a>
              </template>
            </el-table-column>
            <el-table-column label="General" prop="vivo" >
              <template #default="scope">
                <!-- <span >{{scope.row.vivo === 1? "√" : "×"}}</span> -->
                <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
              </template>
            </el-table-column>
            <el-table-column label="Cell-viability" prop="role" >
              <template #default="scope">
                <!-- <span >{{scope.row.role ? "√" : "×"}}</span> -->
                <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
              </template>
            </el-table-column>
            <el-table-column label="Cancer-related" prop="cancer_related" >
              <template #default="scope">
                <!-- <span >{{scope.row.cancer_related > 0 ? "√" : "×"}}</span> -->
                <i v-show="scope.row.cancer_related > 0" class="my-icon-check"></i>
                <i v-show="scope.row.cancer_related === 0" class="my-icon-close"></i> 
              </template>
            </el-table-column>
            <el-table-column label="Disease-related" prop="disease_related" >
              <template #default="scope">
                <i v-show="scope.row.disease_related === 1" class="my-icon-check"></i>
                <i v-show="scope.row.disease_related === 0" class="my-icon-close"></i> 
              </template>
            </el-table-column>
          </el-table>
          <el-pagination
              v-if = "id==1"
              class="pagesearch"
              background 
              v-model:current-page="currentPage"
              v-model:page-size="pageSize"
              @current-change="handleChange"
              layout="prev, pager, next, jumper"
              :total="Total">
            </el-pagination>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { ElRow, ElCol, ElAutocomplete, ElSelect, ElOptionGroup, ElOption, ElButton, ElTable, ElTableColumn, ElPagination } from 'element-plus'
export default {
  emits: ['close'],
  
  components: {
    ElRow,
    ElCol,
    ElAutocomplete,
    ElSelect,
    ElOptionGroup,
    ElOption,
    ElButton,
    ElTable,
    ElTableColumn,
    ElPagination
  },
  data(){
    return {
      currentPage: 1,
      pageSize: 20,
      Total: 0,
      isShow:true,
      lncrnaTable:"",
      inputContent:"",
      searchOpt:"option3",
      options: [
        {
          label:"Query by Organism",
          options:[
            {value:"option1",label:"Human"},
            {value:"option2",label:"Mouse"}
          ]

        },
        {
          label:"Query by essential role",
          options: [
            {value:"option3",label:"General"},
            {value:"option4",label:"Cell viability"},
            {value:"option5",label:"Tumor suppressor"},
            {value:"option6",label:"Oncogene"},
            {value:"option7",label:"Disease related"}
          ]
        }
      ],
      id:0 ,
      url:"https://www.ncbi.nlm.nih.gov/pubmed/?term=",
      urlNCBI:"https://www.ncbi.nlm.nih.gov/gene/",


      properties:[],
      propertyresults:[
        {value: "AIRN"}, {value: "Bvht"}, {value: "Chaserr"},
        {value: "Dlx6os1"}, {value: "Dnm3os"}, {value: "Dreh"}, {value: "Fendrr"}, {value: "Gas5"},
        {value: "Gm12610"}, {value: "Gm2044"}, {value: "Gm38509"}, {value: "Haglr"}, {value: "Hand2os1"},
        {value: "Hdnr"}, {value: "Hm629797"}, {value: "Jpx"}, {value: "Kcnq1ot1"}, {value: "LIVAR"},
        {value: "lncKdm2b"}, {value: "Lncpint"}, {value: "LNCTAM34A"}, {value: "Meg3"}, {value: "MHRT"},
        {value: "Miat"}, {value: "Mir124a-1hg"}, {value: "Neat1"}, {value: "Pantr2"}, {value: "Paupar"},
        {value: "PICSAR"}, {value: "SENCR"}, {value: "Trp53cor1"}, {value: "Tsix"}, {value: "Tslrn1"},
        {value: "Ttc39aos1"}, {value: "Tunar"}, {value: "Xist"},{value: "4933409F18Rik"}, {value: "9030622O22Rik"}, ],


      fuzzyHuman:[],
      fuzzyMouse:[],
      fuzzyVital:[],
      fuzzyTumor:[],
      fuzzyCancer:[],
      fuzzyCell:[],
      fuzzyDisease:[],
      // tempsearpath
      tempPath:""
    }
  },
  methods: {

    kzClick(){
        if(this.isShow){
          this.showData=this.dataList.fasta;
        }
        else{
          this.showData=this.dataList.fasta.slice(0,1000);
        }
        this.isShow=!this.isShow;
    },
    tabRowClassName({ row, rowIndex }) {
      var index = rowIndex + 1;
      if (index % 2 == 0) {
        return "warning-row";
      }
    },
    
    querySearch(queryString, cb) {
      var properties = this.propertyresults;
    
      var results = queryString
        ? properties.filter(this.createFilter(queryString))
        : properties;
        
      cb(results);
    },
    
    createFilter(queryString) {
      return property => {
        
        return (
       
          property.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        );
      };
    },
    fetchData(path){
      var _this = this;
      var sqlPath = "api/property/"+path;

      axios.post(sqlPath,{
        page:_this.currentPage,
        pageSize:_this.pageSize
      }).then(function(respond){
        _this.lncrnaTable=respond.data.items;
        _this.Total = respond.data.total;
        _this.id = 1;
      })
    },
    Search(){
      
      var inputContent = this.inputContent;
      var searchOpt = this.searchOpt;
      var _this = this;
      
      if(searchOpt == "option1"){
        
        if(inputContent == ""){
          _this.tempPath = "selectHuman";
          _this.currentPage = 1;
          _this.fetchData("selectHuman");
          
        }
        
        else{
          axios.post("api/property/searchHuman",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;
          _this.id = 1;
          })
        }
      }
      //option2 Mouse
      else if(searchOpt == "option2"){
        
        if(inputContent == ""){
          _this.tempPath = "selectMouse";
          _this.currentPage = 1;
          _this.fetchData("selectMouse");
         
        }
        
        else{
          axios.post("api/property/searchMouse",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;
          _this.id = 1;
          })
        }
      }
      // option3 reason is vital
      else if(searchOpt == "option3"){
        
        if(inputContent == ""){
          _this.tempPath = "select_reason_vital";
          _this.currentPage = 1;
          _this.fetchData("select_reason_vital");
          
        }
      
        else{
          axios.post("api/property/searchVital",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;
          _this.id = 1;
          })
        }
      }
      // option4 is cell viability
      else if(searchOpt == "option4"){
        
        if(inputContent == ""){
          _this.tempPath = "cellGrowth";
          _this.currentPage = 1;
          _this.fetchData("cellGrowth");
         
        }
        
        else{
          axios.post("api/property/searchCell",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;

          _this.id = 1;
          })
        }
      }

      // option 7 reason is disease
      else if(searchOpt == "option7"){
        
        if(inputContent == ""){
          _this.tempPath = "select_disease_related";
          _this.currentPage = 1;
          _this.fetchData("diseaseRelated");

        }

        else{
          axios.post("api/property/searchDisease",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;
          _this.id = 1;
          })
        }
      }

      else if(searchOpt == "option6"){

        if(inputContent == ""){
          _this.tempPath = "select_reason_tumor";
          _this.currentPage = 1;
          _this.fetchData("select_reason_tumor");

        }

        else{
          axios.post("api/property/searchTumor",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;

          _this.id = 1;
          })
        }
      }
      
      //option 5 reason is cancer
      else if(searchOpt == "option5"){

        if(inputContent == ""){
          _this.tempPath = "select_reason_cancer";
          _this.currentPage = 1;
          _this.fetchData("select_reason_cancer");
          
         
        }

        else{
          axios.post("api/property/searchCancer",{inputContent}).then(function(respond){
          _this.lncrnaTable=respond.data;
          _this.id = 1;
          })
        }
      }




    },
    toUrl_NONCODE(data){
      window.location.href = "http://www.noncode.org/show_gene.php?id="+data.split(".")[0]+"&version="+data.split(".")[1]+"&utd=1#"
    },
    toUrl_LncBook(data){
      window.location.href = "https://ngdc.cncb.ac.cn/lncbook/gene?geneid="+data
    },
    toUrl_NCBI(data){
      window.location.href = "https://www.ncbi.nlm.nih.gov/gene/"+data
    },
    toUrl(data){
      

      sessionStorage.setItem('dataSearch', JSON.stringify(data));
      this.$router.push({
        name:'Gene',
        params:data,
        query:{page:"Search"}
      })

    },
    handleChange(newPage,path) {

      this.currentPage = newPage;
      this.fetchData(this.tempPath);
    }
    
  },

  mounted () {
    var _this = this;
    axios
      .all([
        axios.post("/v2/api/property/fuzzyHuman"),
        axios.post("/v2/api/property/fuzzyMouse"),
        axios.post("/v2/api/property/fuzzyVital"),
        axios.post("/v2/api/property/fuzzyTumor"),
        axios.post("/v2/api/property/fuzzyCancer"),
        axios.post("/v2/api/property/fuzzyCell"),
        axios.post("/v2/api/property/fuzzyDisease")
      ])
      .then(
        axios.spread((human, mouse,vital ,tumor,cancer,cell,disease) => {
          for (let i = 0;i< human.data.length;i++){
          _this.fuzzyHuman.push({
          "value":human.data[i]["gene_name"]
          })
        }
          for (let i = 0;i< mouse.data.length;i++){
          _this.fuzzyMouse.push({
          "value":mouse.data[i]["gene_name"]
          })
        }
          for (let i = 0;i< vital.data.length;i++){
          _this.fuzzyVital.push({
          "value":vital.data[i]["gene_name"]
          })
        }

          for (let i = 0;i< tumor.data.length;i++){
          _this.fuzzyTumor.push({
          "value":tumor.data[i]["gene_name"]
          })
        }   
          for (let i = 0;i< cancer.data.length;i++){
          _this.fuzzyCancer.push({
          "value":cancer.data[i]["gene_name"]
          })
        }  
          for (let i = 0;i< cell.data.length;i++){
          _this.fuzzyCell.push({
          "value":cell.data[i]["gene_name"]
          })
        }
          for (let i = 0;i< disease.data.length;i++){
          _this.fuzzyDisease.push({
          "value":disease.data[i]["gene_name"]
          })
        }
        })
      );
  },
  watch: {

    searchOpt(val){

      var searchOpt = val;
      var _this = this;

      if (searchOpt == "option1") {
        _this.propertyresults = _this.fuzzyHuman;
      }
      else if (searchOpt == "option2") {
        _this.propertyresults =  _this.fuzzyMouse;
        
      } else if (searchOpt == "option3" ) {
       
        _this.propertyresults =  _this.fuzzyVital;

      } 
      else if (searchOpt == "option4") {
        _this.propertyresults =  _this.fuzzyCell;
      }
      else if (searchOpt == "option5") {
        _this.propertyresults =  _this.fuzzyTumor;
      }
      else if (searchOpt == "option6") {
        _this.propertyresults =  _this.fuzzyCancer;
      }
      else if (searchOpt == "option7") {
        _this.propertyresults =  _this.fuzzyDisease;
      }
    }

  }

}
</script>

<style>
/* 没有用scoped 如果使用斑马线设置无效 */
.header {
  width: 100%;
  padding-bottom: 60px;
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
  ); 
  background: linear-gradient(
    135deg,
    #e6f0ef 45%,
    #b4ede7 100%
  ); 
}
.title{
 
  justify-content: center;
  align-items: center;
  line-height: 80px;
}
.input-with-select {
  width: 80%;
  /* font-size: 15px; */
}
.el-collapse-item__header {
  font-size: 16px;
}

.el-select {
  width: 220px;
}

.el-select-group__title {
  padding-left: 0;
  text-align: center;
  font-size:16px;
  font-family:monospace;
}

.el-select-dropdown__item {
  text-align: center;
  text-indent: 2em;
}

.el-input {
  font-size: 15px;
}

.content {
  padding: 10px;
  width: 90%;
  margin: 0 auto;
}



.el-table .warning-row {
  background: #ccf1f1;
}
.tabletitle {
  text-align: center;
  background-color: #99cccc;
  height: 30px;
  line-height: 30px;
  color: #686868;
  font-weight: bold;
}
.explain {
  /* border: solid 1px #99cccc; */
  padding: 10px;
  width: 70%;
}
.explain p {
  text-indent: 2em;
  text-align: justify;
  font-family: Arial, "Microsoft YaHei", "微软雅黑", serif;
}


.el-input__prefix, .el-input__suffix{
  text-align: right;
}
.span_style{
  background:#f2f4f6;
  width:70%;
  font-family:monospace;
}
.wrapper{
  display:flex;
  align-items:center;
  padding-left:10px;
}
.pagesearch{
  margin-top: 10px;
  text-align: center;
}

.my-icon-check {
  display: inline-block;
  width: 20px;
  height: 20px;
  background-image: url('/v2/assets/img/selected.svg');
  background-size: contain;
  background-repeat: no-repeat;
}
.my-icon-close {
  display: inline-block;
  width: 20px;
  height: 20px;
  background-image: url('/v2/assets/img/not_selected.svg');
  background-size: contain;
  background-repeat: no-repeat;
}
</style>