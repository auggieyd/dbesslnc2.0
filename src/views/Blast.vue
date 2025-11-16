<template>
  <div>
    <el-row class="title" style="color: #606060;">
    <img style="margin-right: 20px; height: 55px; width: 55px;vertical-align: middle;" 
         src="../../public/assets/img/blast.png" />
      Blast
    </el-row>
    <div class="myForm" >
      <el-input 
      class="RNAinput" 
      type="textarea" 
      rows="10" 
      placeholder="Enter the query lncRNA sequence(FASTA)" 
      v-model="textarea" 
      clearable></el-input>
      <div  style="margin-top: 20px">
        <b class="sou" >e-value: </b>
        <el-select v-model="eValue" clearable @change="evalue_change" style="margin: 0 20px 0 10px">
        <el-option v-for="item in options1" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>
        <b class="sou" >word size: </b>
        <el-select v-model="word_size" clearable @change="word_change" style="margin: 0 20px 0 10px">
        <el-option v-for="item in options2" :key="item.value" :label="item.label" :value="item.value"></el-option>
        </el-select>


        <el-button 
        class="sou" 
        type="success" 
        v-on:click="Search(eValue,word_size)" 
        style="margin-left: 10px; padding-left: 10px" 
        icon="el-icon-search" plain>Blast</el-button>
        <el-button 
        class="sou" 
        v-on:click="SearchExample()" 
        plain>Example</el-button>
       

        <el-table
          :data = "pageData"
          v-show="isShow"
          border
          stripe
          style = "width:100%;margin:20px auto 0 auto"
          row-key="indexID"
          strip highlight-current-row
          @expand-change="handleExpandChange">
          <el-table-column  type="expand"  label="Detail" width="80"> 
            <template #default="props" >
              
              <div class="expand-loading-wrap">
              <p v-if="props.row.loading" v-loading="props.row.loading" style="text-align: center;">loading...</p>

              <el-form v-else label-position="left" inline class="demo-table-expand" >
                <el-form-item label="Organism:">
                  <span>{{props.row.Organism}}</span>
                </el-form-item>
                <el-form-item label="Gene UID:">
                  <span @click="toUrl_DNA(props.row)" class="hand">{{ props.row.UID }}</span>
                </el-form-item>
                <el-form-item label="transcript_id:">
                  <span @click="toUrl_RNA(props.row.transcript_id)" class="hand">{{ props.row.transcript_id }}</span>
                </el-form-item>
                <el-form-item label="Position:" >
                  <span>{{props.row.position}}</span>
                </el-form-item>
                <el-form-item label="LncRNA Sequence Length:" >
                  <span>{{props.row.Seqlength}}</span>
                </el-form-item>
                <el-form-item label="Sequence:" >
                  <span class="newlist_blast" v-html="props.row.showData" @click="kzClick($event,props.row)">
                  </span>
                </el-form-item>
              </el-form>
              </div>
            </template>
          </el-table-column>
          <el-table-column
            label="Subject seq id"
            prop="sseqid"
            width="230">
          </el-table-column>
          <el-table-column
                label="Percentage(identical matches)"
                prop="pident"
                width="250" >
          </el-table-column>
          <el-table-column
            label="Alignment length"
            prop="length"
            width="180">
          </el-table-column>

          <el-table-column
            label="e-value"
            prop="evalue">
          </el-table-column>
          <el-table-column
            label="Bitscore"
            prop="bitscore">
          </el-table-column>
        </el-table>    
        <el-pagination
          v-if = "isShowPage"
          class="pagesearch"
          background 
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          @current-change="handlePageChange"
          layout="prev, pager, next, jumper"
          :total="Total">
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ElLoading } from 'element-plus'

export default {
  data() {
    return {
      example: `>TCONS_00106247
CTCTAGAGGCTTGCGTCCCGGGAGCCCGGCCTCGTGCGCCGCGCTTTGAGCAGCAGACTGCTCGACAAACACTGCGCCAAGAGCTCCTCAGCAGAAGCTCCTCGCATCAGATCCTCTGTGCTGGGAATCCTCCCCTCTTGAGCACACTCTGTGCTCCTCTTCCAGTTACGGTGCATGTGAAGCAATGGTATGGGAAAATTGTTTGCAGAAGGATGAAAAGGCTTTATTGCCAAACTGAACACAGGACTCACCGCTGTAGATACTTGCAGAAGCACTGAAGCTCCTGGAGGGTCTCCTTTGCAGTCTGGAAGATTTCCTCCACGAGAAACAAGTCCACTAAGTGGGCACAGACATCCTCACAGCAACGGGCCACACGGACCCTCTGGTCTGTCTCTACTGCATTCCTAGAAACAGGGCAATCAGCATGGAAGACACTGCACTTGGGGCCCACAGACACTGAGGGCTTGCTTGAAAAGTGCAAGAGTCAGTCAGGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGAAGGCCGAAGCGGGTGGATCATGAGGTCAAGAGATCCAGACCATCCTGGCTAACATGGTGAAACCCTGTCTCTACTAAAAATACAAAAAAATTAGCCTGGTGTGGTGGCGGGCGCCTGTAGTCCCAGCTACTCGGGAGGCTGAAGCAGGAGAATGACGTGAAGCCGGGAGGCAGA`,
      textarea: '',
      
      word_size:'11',
      options2:[
       {value:'5',label:'5'},
       {value:'6',label:'6'},
       {value:'7',label:'7'},
       {value:'8',label:'8'},
       {value:'9',label:'9'},
       {value:'10',label:'10'},
       {value:'11',label:'11'}],
      // 设置eValue下拉框选项
      options1: [
          {
          value: '1e-3',
          label: '1e-3'
          },{
          value: '1e-4',
          label: '1e-4'
          },{
          value: '1e-5',
          label: '1e-5 '
          },{
          value: '1e-6',
          label: '1e-6 '
          },{
          value: '1e-7',
          label: '1e-7 '
          }],
      // 设置eValue默认值
      eValue: '1e-7',
      resData:[],
      tableData:[],     
      isShow:false,
      length:1,
      RNAID:"",
      SeqData:{},
      currentPage: 1,
      pageSize: 10,
      Total: 0,
      isShowPage: false
    }
  },
  computed: {
    pageData() {
      const start = (this.currentPage - 1) * this.pageSize;
      return this.tableData.slice(start, start + this.pageSize);
    }
  },
  methods: {
    kzClick(event,row){      

        if(event.target.className === 'open' && event.target.nodeName === 'IMG'){
                row.showData = `${row.Sequence}
                    <img
                    src="/v2/assets/img/close.png"
                    style="width:12px; height:12px"
                    class="close"
                    />
                    `
        }
        if(event.target.className === 'close' && event.target.nodeName === 'IMG'){
                row.showData = `${row.Sequence.slice(0,200)}
                    <img
                    src="/v2/assets/img/open.png"
                    style="width:12px; height:12px"
                    class="open"
                    />
                    `
        }

    },
    handleExpandChange(row, expanded) {
      if (expanded.length ) {
        row.loading = true; 
        axios.post("api/property/fuzzySeq", {
          alignId: row.sseqid
        }).then(res => {
          const detail = Array.isArray(res.data) ? res.data[0] : res.data
          row.UID = detail.UID
          row.transcript_id = detail.transcript_id
          let chr = detail.chr
          let start = detail.start
          let end = detail.end
          let strand = detail.strand === '-' ? "reverse" : "forward"
          let version =  detail.Organism === 'Human' ?"(hg38)":"(mm10)"
          let position = chr + ":" + start + "-" + end + "," + strand + version
          let Sequence = detail.FASTA
          let Seqlength = detail.length
          row.position = position
          row.Seqlength = Seqlength
          row.Sequence = Sequence
          row.showData = `${Sequence.slice(0,200)}
                    <img
                    src="/v2/assets/img/open.png"
                    style="width:12px; height:12px"
                    class="open"
                    />`
          row.Organism = detail.Organism
        }).finally(() => {
          row.loading = false; // 
        })
      }
    },
    handlePageChange(val) {
      this.currentPage = val;
    },
    SearchExample(){
      //显示example数据
      this.textarea = this.example;
    },
    evalue_change(val){
      this.eValue = val;
    },
    word_change(val){
      this.word_size = val;
    },
    Search(eValue,word_size){

      const loadingInstance = ElLoading.service({
        fullscreen:true,
        text:"Loading...",
        background:"rgba(0,0,0,0.7)"
      });
      this.isShowPage = true
      var _this = this
      _this.isShow = true
      axios.post("api/property/blast",{
          user_seq: _this.textarea,
          user_wordSize: word_size,
          user_eValue: eValue
      }).then(respond =>{
        
        _this.resData=respond.data.message.data
        _this.length=respond.data.message.data.length
        if(_this.length == 1){
          window.alert("Blast query is Empty or FASTA sequence format error!")
          loadingInstance.close() 
        }
        else{
          let stuID = []
          for(let i = 0;i < _this.length-1;i++){            
            if(_this.resData != ""){
              stuID.push(_this.resData[i].split("\t")[1].split("|")[0])                                                     
            }           
          }
          _this.RNAID = "'"+stuID.join("','")+"'"
        }
        for(let j = 0; j < _this.length-1 ; j++){        
            let sseqid = _this.resData[j].split('\t')[1].split('|')[0]
            let pident = _this.resData[j].split('\t')[2]
            let length = _this.resData[j].split('\t')[3]
            let evalue = _this.resData[j].split('\t')[4]
            let bitscore = _this.resData[j].split('\t')[5].split('\r')[0]

            let result = {
              "indexID":j+sseqid,
              "sseqid":sseqid,
              "pident":pident,
              "length":length,
              "evalue":evalue,
              "bitscore":bitscore,
              "UID": '',
              "transcript_id": '',
              "position": '',
              "Seqlength": '',
              "Sequence": '',
              "Organism": ''
            }
            _this.tableData.push(result)
        }

        loadingInstance.close() 
      }).finally(() => {
        // 计算总条数
        _this.Total = _this.tableData.length;
        _this.currentPage = 1; 
        // 如果没有数据，提示用户
        if (_this.Total === 0) {
          window.alert("No results found for the given query.");
        }
      }).catch(error => {
        console.error("Error during search:", error);
        loadingInstance.close();
      });
    },

    toUrl_DNA(data){
      sessionStorage.setItem('dataBlast', JSON.stringify(data));
      this.$router.push({
        name:'Gene',
        params:data,
        query:{page:"Blast"}
      })
    },
    toUrl_RNA(data){
      this.$router.push({
        name:'Visual',
        params:{data},
        query:{page:"Blast"}
      })
    }

  }
}

</script>

<style scoped>
.el-select{
  width: 150px !important;
}
.el-input{
  width: 150px;
}
.el-select-dropdown__item{
  text-align: center !important;
}
</style>
<style scoped lang="less">
.myForm {
  margin: 10px auto; /* 表单居中设置 */
  padding: 40px 60px;
  width: 75%;
  border: 3px solid #b4ede7;
  border-radius: 10px;
}

.el-table {
  font-size: 15px;
  white-space: pre-line;
  //color: #232324;
}
// .demo-table-expand {
//     font-size: 0;
// }
.demo-table-expand label {
  width: auto;
  font-size:16px;
  font-weight:bold;
}
.demo-table-expand {
  margin-right: 0;
  margin-bottom: 0;
  width: 100%;
}
:deep(.el-form-item__label) {
  font-size: 15px;
  //color: #232324;
}

.title {
  text-align: center;
  font-size: 1.5em;
  line-height: 80px;
  height: 80px;
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

.el-form-item {
  border-top: 1px solid #ebeef5; // 表格线条颜色
  margin-bottom: 0;
}



// /deep/ 相当于 >>>
:deep(.el-input__inner:hover) {
  // background-color: rgb(115, 200, 200) !important;
  border-color: rgb(115, 200, 200) !important;
}

:deep(.el-input .is-active .el-input__inner.el-input__inner:focus)  {
  border-color: rgb(115, 200, 200) !important;
}

:deep( .el-radio__inner:hover) {
  background-color: rgb(115, 200, 200) !important;
  border-color: rgb(115, 200, 200) !important;
}
// 单选框的标签可以换行了
:deep(.all_label)  {
  display: inline-grid;
  white-space: pre-line;
  word-wrap: break-word;
  overflow: hidden;
  line-height: 20px;
}
:deep(.el-checkbox__input.is-checked + .el-checkbox__label) {
  color: rgb(115, 200, 200) !important;
}
:deep(.el-checkbox__input.is-checked .el-checkbox__inner)  {
  background-color: rgb(115, 200, 200) !important;
  border-color: rgb(115, 200, 200) !important;
}
:deep(.el-checkbox__label){
  padding-left: 5px;
}
:deep(.el-radio__input.is-checked + .el-radio__label)  {
  color: rgb(115, 200, 200) !important;
}
:deep(.el-radio__input.is-checked .el-radio__inner){
  background-color: rgb(115, 200, 200) !important;
  border-color: rgb(115, 200, 200) !important;
}
:deep(.el-radio__label) {
  padding-left: 5px;
  font-size: 15px;
  color: #232324;
}
:deep(.el-textarea__inner){
  border-color: rgb(115, 200, 200) !important;
  font-size: 15px;
  color: #232324;
}
:deep(.el-select .el-input__inner:focus)  {
  border-color: rgb(115, 200, 200);
}

.el-select {
  margin-left: 10px;
}

.el-select-dropdown__item.selected {
  color: rgb(115, 200, 200);
}

.el-select-dropdown__item {
  text-align: center;
  text-indent: 0;
}


// 遮盖原始按钮，以改变原始按钮的样式
.upload {
  height: 35px;
  line-height: 35px;
  //   position: relative;
  font-size: 15px;
  width: 100px;
  border-radius: 5px;
  color: #fff;
  background-color: #5cb85c;
  margin: auto 30px;
  outline: none;
  cursor: pointer;
}

// 选择文件的原始按钮
.change {
  position: absolute;
  overflow: hidden;
  width: 100px;
  line-height: 35px;
  left: 30px;
  top: 20px;
  opacity: 0; // 设为透明
  cursor: pointer;
}

.submit {
  font-size: 15px;
  height: 35px;
  width: 120px;
  border-radius: 5px;
  color: #fff;
  background-color: #337ab7;
  border: #337ab7;
  margin: auto 10px; // 按钮居中
  outline: none;
  cursor: pointer;
}

.myemail {
  font-size: 15px;
  height: 35px;
  width: 120px;
  border-radius: 5px;
  color: #fff;
  background-color: #e6a23c;
  border: #e6a23c;
  margin: 10px 10px 10px; // 按钮居中
}

.progress-wrap {
  width: 100%;
  margin: 0 auto;
  // border-left: 1px solid #ebeef5;
  p {
    margin: 0 auto;
    width: 100%;
    font-size: 15px;
  }
  .progress {
    background-color: #c5c8ce;
    height: 15px;
    span {
      display: block;
      background-color: #19be6b;
      height: 100%;
      width: 0;
    }
  }
}
span {
  display:inline-block;
  // 在span标签中，可设置输出的内容截断 
  word-wrap:break-word; 
  word-break: break-all; 
  white-space:normal ; 
  width:100%;
  font-size:15px;
  font-family:"Avenir", Helvetica, Arial, sans-serif;
} 

.hand:hover{
  color:#1ee3cf;
  cursor:pointer
}
.newlist {
  position: relative;
  margin: 0 auto;
  width: 80%;
  min-height: 30px;
  line-height: 20px;
  /* border: 1px solid ; */
  word-break: break-all;
  hyphens: auto;
  text-align: left;
  padding: 5px 10px;
  background:#f2f4f6;
  font-family:monospace;
}
.newlist_blast {
  
  margin: 10px auto;
  width: 80%;
  min-height: 30px;
  line-height: 20px;
  /* border: 1px solid ; */
  word-break: break-all;
  hyphens: auto;
  text-align: left;
  padding: 5px 10px;
  background:#f2f4f6;
  font-family:monospace;
}
.open_style{
  height:18px;
  width:18px;
}
.sou{
  font-weight:700;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size:15px;

}
/deep/ .el-button span {
  font-weight:700;
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  font-size:15px;
}
.example-showcase .el-loading-mask {
  position: relative;
  z-index: 9;
}
</style>
