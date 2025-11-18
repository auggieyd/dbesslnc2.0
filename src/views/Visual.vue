<template>
    <div>
        <el-row class="title" style="color: #606060;">
          <img
          src="../../public/assets/img/back.png"
          class="img_style"
          
          @click="toUrl()"
         />
            <p>Detail information of {{dataList.transcript_id}}</p>

        </el-row>
        <div class="files">
          <h3 class="top">LncRNA Information</h3>
          <div class="content" style="height:40%">
            <el-form label-position="left"  inline class="demo-table-expand" >
              <el-form-item label="Gene:">
                <span>{{ dataList.UID}}</span>
              </el-form-item>
              <el-form-item label="Organism:">
                <span>{{ dataList.Organism }}</span>
              </el-form-item>
              <el-form-item label="LncBook:" >
                  <span>
                    {{ dataList.Lncbook_trans_id !== 'N.A.' ? 'transcript:&nbsp':'' }} 
                    {{  dataList.Lncbook_trans_id }}
                    {{ dataList.Lncbook_id !== 'N.A.' ? ',&nbspgene:&nbsp ':'' }}
                    <text
                      v-if="dataList.Lncbook_id !== 'N.A.'"
                      @click="toUrl_LncBook(dataList.Lncbook_id)"
                      class="hand">
                      {{ dataList.Lncbook_id }}
                    </text>   
                  </span>  
              </el-form-item>
              <el-form-item label="NONCODE:">
                <span>
                    {{ dataList.Noncode_trans_id !== 'N.A.' ? 'transcript:&nbsp':'N.A.' }} 
                    <text
                      v-if="dataList.Noncode_trans_id!== 'N.A.'"
                      @click="toUrl_RNA(dataList.Noncode_trans_id)"
                      class="hand">
                      {{ dataList.Noncode_trans_id }}
                    </text>
                    {{ dataList.Noncode_trans_id !== 'N.A.' ? ',&nbspgene:&nbsp ':'' }}
                    <text
                      v-if="dataList.Noncode_id !== 'N.A.' && dataList.Noncode_trans_id !== 'N.A.'"
                      @click="toUrl_DNA(dataList.Noncode_id)"
                      class="hand">
                      {{ dataList.Noncode_id }}
                    </text>   
                  </span>  
              </el-form-item>

              <el-form-item label="Chromosome:">
                <span>{{ dataList.chr}}</span>
              </el-form-item>
              <el-form-item label="Start:">
                <span>{{ dataList.start }}</span>
              </el-form-item>
              <el-form-item label="End:">
                <span>{{ dataList.end }}</span>
              </el-form-item>
              <el-form-item label="Strand:">
                <span>{{ dataList.strand }}</span>
              </el-form-item>
              <el-form-item label="Length:">
                <span>{{ dataList.length}}</span>
              </el-form-item>
              <el-form-item label="exon number:">
                <span>{{ dataList.exon_num }}</span>
              </el-form-item>
              <el-form-item label="exon position:">
                <span>{{ dataList.exon_pos }}</span>
              </el-form-item>
              <el-form-item label="Sequence:" >
                <!-- <el-button type="primary" size="small" @click="kzClick($event)">load Sequence</el-button> -->
                <span  class="newlist" v-html="this.showData" @click="kzClick($event)" ></span> 
              </el-form-item>
            </el-form>
          </div>

        </div>
        <div class="files">
          <h3 class="top">Expression Profile</h3>
          <!-- human -->
          <div v-show="isShow" class="content" style="height:40%">
            <span>N.A.</span>
          </div> 
          <div v-show="isShow1" class="content" style="height:40%" id="outerDiv1">
            <!-- 第一个表 -->
            <el-table :data="profile" :header-cell-style="{background:'rgb(115, 200, 200)',color:'#fff'}" style="width: 100%">
              <el-table-column prop="brain" label="brain"></el-table-column>
              <el-table-column prop="lung" label="lung"></el-table-column>
              <el-table-column prop="urinarybladder" label="urinarybladder"></el-table-column>
              <el-table-column prop="kidney" label="kidney"></el-table-column>
              <el-table-column prop="adrenal" label="adrenal"></el-table-column>
              <el-table-column prop="thyroid" label="thyroid"></el-table-column>
              <el-table-column prop="heart" label="heart"></el-table-column>
            </el-table>
          
            <!-- 第二个表 -->
            <el-table :data="profile" :header-cell-style="{background:'rgb(115, 200, 200)',color:'#fff'}" style="width: 100%">              
              <el-table-column prop="lymphnode" label="lymphnode"></el-table-column>
              <el-table-column prop="spleen" label="spleen"></el-table-column>
              <el-table-column prop="bonemarrow" label="bonemarrow"></el-table-column>
              <el-table-column prop="tonsil" label="tonsil"></el-table-column>
              <el-table-column prop="appendix" label="appendix"></el-table-column>
              <el-table-column prop="colon" label="colon"></el-table-column>
              <el-table-column prop="esophagus" label="esophagus"></el-table-column>
            </el-table>
          
            <!-- 第三个表 -->
            <el-table :data="profile" :header-cell-style="{background:'rgb(115, 200, 200)',color:'#fff'}" style="width: 100%">             
              <el-table-column prop="gallbladder" label="gallbladder"></el-table-column>
              <el-table-column prop="smallintestine" label="smallintestine"></el-table-column>
              <el-table-column prop="salivarygland" label="salivarygland"></el-table-column>
              <el-table-column prop="stomach" label="stomach"></el-table-column>
              <el-table-column prop="liver" label="liver"></el-table-column>
              <el-table-column prop="duodenum" label="duodenum"></el-table-column>
              <el-table-column prop="pancreas" label="pancreas"></el-table-column>
            </el-table>
          
            <!-- 第四个表 -->
            <el-table :data="profile" :header-cell-style="{background:'rgb(115, 200, 200)',color:'#fff'}" style="width: 100%">
              <el-table-column prop="rectum" label="rectum"></el-table-column>
              <el-table-column prop="endometrium" label="endometrium"></el-table-column>
              <el-table-column prop="ovary" label="ovary"></el-table-column>
              <el-table-column prop="testis" label="testis"></el-table-column>
              <el-table-column prop="prostate" label="prostate"></el-table-column>
              <el-table-column prop="fallopiantube" label="fallopiantube"></el-table-column>
              <el-table-column prop="skeletalmuscle" label="skeletalmuscle"></el-table-column>
            </el-table>
          
            <!-- 第五个表 -->
            <el-table :data="profile" :header-cell-style="{background:'rgb(115, 200, 200)',color:'#fff'}" style="width: 100%">
              <el-table-column prop="smoothmuscle" label="smoothmuscle"></el-table-column>
              <el-table-column prop="skin" label="skin"></el-table-column>
              <el-table-column prop="fat" label="fat"></el-table-column>
            </el-table>
            <div id ="figure1"></div>
          </div>
          <!-- mouse -->
          <div v-show="isShow2" class="content" style="height:40%" id="outerDiv2">
            <el-table :data="profile"  :header-cell-style="{background:'rgb(115, 200, 200)',color:'#fff'}" style="width: 100%" >
              <el-table-column prop="adipose" label="heart" ></el-table-column>
              <el-table-column prop="adrenal" label="hippocampus" ></el-table-column>
              <el-table-column prop="brain" label="liver" ></el-table-column>
              <el-table-column prop="brain_R" label="lung" ></el-table-column>
              <el-table-column prop="breast" label="spleen" ></el-table-column>
              <el-table-column prop="colon" label="thymus"></el-table-column>
            </el-table>
            <div id="figure2"></div>
          </div>
        </div>

    </div>
</template>

<script>
import axios from "axios";

// 引入 ECharts 核心模块和图表/组件
import * as echarts from 'echarts';


import {
  ElRow,
  ElForm,
  ElFormItem,
  ElTable,
  ElTableColumn
} from 'element-plus';
export default{
  name: 'VisualPage',
  components: {
    ElRow,
    ElForm,
    ElFormItem,
    ElTable,
    ElTableColumn
  },
    data(){
      return{
        dataList:{},
        isShow:true,
        showData:"",
        profile:[],
        formatedData:[],
        RNAid:"NONHSAT000530.2",
        UID:"",
        Organism:"Human",
        item_data_human: [
          'brain', 'lung', 'urinarybladder', 'kidney', 'adrenal', 'thyroid', 'heart', 
          'lymphnode', 'spleen', 'bonemarrow', 'tonsil', 'appendix', 'colon', 
          'esophagus', 'gallbladder', 'smallintestine', 'salivarygland', 'stomach', 
          'liver', 'duodenum', 'pancreas', 'rectum', 'endometrium', 'ovary', 'testis', 
          'prostate', 'fallopiantube', 'skeletalmuscle', 'smoothmuscle', 'skin', 'fat'
        ],
        item_data_mouse:['adipose', 'adrenal', 'brain', 'brain_R', 'breast', 'colon'],
        isShow1:false,
        isShow2:false,
        FromPage:""
      
      }
    },
    mounted(){

      let sessionData = JSON.parse(sessionStorage.getItem("dataGene"));
      
      if(location.href.indexOf('#reloaded')==-1){
      location.href=location.href+"#reloaded";
        location.reload();
      }
     
      this.FromPage = this.$route.query.page;
      this.dataList=sessionData;
      this.showData = `${this.dataList.FASTA.slice(0,200)}
                    <img
                    src="/v2/assets/img/open.png"
                    style="width:12px; height:12px"
                    class="open"
                    />
                    `
    
      this.RNAid=sessionData.transcript_id;
      this.UID=sessionData.UID;
      this.Organism = sessionData.Organism;

      axios.post("api/property/profiles",{    
        RNAid:this.RNAid,
        UID:this.UID,
        Organism:this.Organism
      }).then(respond =>{
        const temp_value =respond.data;
        temp_value.map(row => {
          this.item_data_human.forEach(item => {
            row[item] = parseFloat(row[item]).toExponential(6);
          });
        })
        this.profile = temp_value;
        if(this.profile.length == 0){
          this.isShow=true;
        }
        else if( this.profile.length != 0 && this.profile[0].Organism == "Human"){
          
          this.isShow1=true;
          this.isShow=false;
          this.$nextTick(()=>{
            this.drawLine1();
          })
          // this.drawLine1();
        }
        else{

          this.isShow2=true;
          this.isShow=false;
          this.drawLine2();
        }      
      });
      

    },
    methods:{

      kzClick(event){      
        if(event.target.className === 'open' && event.target.nodeName === 'IMG'){
                this.showData = `${this.dataList.FASTA}
                    <img
                    src="/v2/assets/img/close.png"
                    style="width:12px; height:12px"
                    class="close"
                    />
                    `
        }
        if(event.target.className === 'close' && event.target.nodeName === 'IMG'){
                this.showData = `${this.dataList.FASTA.slice(0,200)}
                    <img
                    src="/v2/assets/img/open.png"
                    style="width:12px; height:12px"
                    class="open"
                    />
                    `
        }

      },
      drawLine1(){

        var chartDom = document.getElementById('figure1');
        var myChart1 = echarts.init(chartDom, null, { renderer: 'svg' });
        var _this = this;
        var option;
        option = {
          title: {
            text: 'Expression profile',
            left: 'center'
          },
  
          tooltip:{
            trigger:'axis',
            axisPointer:{
              type:'shadow'
            }
          },
          xAxis: {
            type: 'category',
            data:this.item_data_human,
              axisLabel: {
                interval: 0,
                rotate:35
            }
          },
          yAxis: {
            type: 'value',
            name:"TPM",     
          },
          series: [
            {
              data: [],
              type: 'bar',
              barCategoryGap:15
            }
          ]
        };
        option.series[0].data=[];
        option.title.text="Expression profile of "+ this.dataList.transcript_id+" in "+this.profile[0].Organism+" tissues";
        _this.item_data_human.forEach(item=>{
          const value = parseFloat(_this.profile[0][item]);
          const formattedValue = value.toExponential(6);

          option.series[0].data.push(formattedValue);
        })
        myChart1.setOption(option);
        window.addEventListener('resize', myChart1.resize);
        
      },
      drawLine2(){
        
        var chartDom = document.getElementById('figure2');
        var myChart2 = echarts.init(chartDom);
        var option;
        option = {
          title: {
            text: 'Expression profile',
            left: 'center'
          },
          tooltip:{
            trigger:'axis',
            axisPointer:{
              type:'shadow'
            }
          },
          xAxis: {
            type: 'category',
            data:['heart', 'hippocampus', 'liver', 'lung', 'spleen', 'thymus'],
              axisLabel: {
                interval: 0,
                rotate:15
            }
          },
          yAxis: {
            type: 'value',
            name:"FPKM/TPM",     
          },
          series: [
            {
              data: [],
              type: 'bar',
              barCategoryGap:20
            }
          ]
        };
        option.series[0].data=[];
        option.title.text="Expression profile of "+ this.dataList.NONCODE_TRANSCRIPT_ID+" in "+this.profile[0].organism+" tissues"
        this.item_data_mouse.forEach(item=>{
          option.series[0].data.push(this.profile[0][item]);
        })
        myChart2.setOption(option);

      },
      toUrl(){
        this.$router.push({
          name:'Gene',
          query:{page:this.FromPage}

        })
      },
      toUrl_RNA(data){
          window.location.href = "http://www.noncode.org/show_rna.php?id="+data.split(".")[0]+"&version="+data.split(".")[1]+"&utd=1#"

      },
      toUrl_DNA(data){
         window.location.href = "http://www.noncode.org/show_gene.php?id="+data.split(".")[0]+"&version="+data.split(".")[1]+"&utd=1#"
      },
      toUrl_LncBook(data){
        window.location.href = "https://ngdc.cncb.ac.cn/lncbook/gene?geneid="+data
      },
      // toImg(data){
      //   this.ShowImg=!data;
      // }

 
      
    }
 
}
</script>

<style scoped>


#figure1{
  width: 100%; 
  height:500px;
  display: inline-block;
  text-align: center;
  margin:20px auto;

}
#figure2{
  width: 1000px; 
  height:500px;
  display: inline-block;
  text-align: center;
  margin:0 auto;

}


.open_style{
  height:18px;
  width:18px;
}
button{
  font-size:15px;
  font-family:"Avenir", Helvetica, Arial, sans-serif;
  margin-left: 10px; 
  padding-left: 10px;
  background-color: #5bd1d7;
  border:none;
  border-radius: 10px;
}
:deep(.el-form-item__label) {
  /* font-size: 15px; */
  font-weight: bold;
  color: #99A9BF;
}
</style>