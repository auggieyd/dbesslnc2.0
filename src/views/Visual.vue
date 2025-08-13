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
            <el-form label-position="left"  inline >
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
import echarts from "echarts";
export default{
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
      // console.log(sessionData,"sessionData")
      
      if(location.href.indexOf('#reloaded')==-1){
      location.href=location.href+"#reloaded";
        location.reload();
      }
     
      this.FromPage = this.$route.query.page;
      //console.log("visual页面的，标记从哪里来",this.FromPage)
      this.dataList=sessionData;
      //console.log(this.dataList)
      // this.showData=this.dataList.FASTA.slice(0,1000);
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
        // console.log(respond.data);
        const temp_value =respond.data;
        // console.log(respond.data,"profile")
        temp_value.map(row => {
          this.item_data_human.forEach(item => {
            row[item] = parseFloat(row[item]).toExponential(6);
          });
        })
        this.profile = temp_value;
        console.log(this.profile,"this.profile")
        if(this.profile.length == 0){
          this.isShow=true;
        }
        else if( this.profile.length != 0 && this.profile[0].Organism == "human"){
          
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
        console.log("调用dramLine1");
                // 解决数据初始渲染不出来的问题
        // setTimeout(()=>{
        //     this.initChart()
        // },1000)
        var chartDom = document.getElementById('figure1');
        var myChart1 = echarts.init(chartDom, null, { renderer: 'svg' });
        var _this = this;
        var option;
        option = {
          title: {
            text: 'Expression profile',
            left: 'center'
          },
    //        toolbox: {
    //     show: true, // 显示工具箱
    //     feature: {
    //         saveAsImage: { // 保存为图片功能
    //             show: true, // 显示保存图片按钮
    //             title: '保存为图片' ,// 按钮标题
    //             type: 'svg',
    //             // name: '自定义文件名'
    //         },
    //         // 如果需要其他功能，可以在这里添加，例如：
    //         // dataView: {show: true, readOnly: false, title: '数据视图'},
    //         // restore: {show: true, title: '还原'},
    //         // dataZoom: {show: true, title: {zoom: '区域缩放', back: '区域缩放还原'}}
    //     },
    //     right: 20, // 工具箱距离右侧的距离
    //     top: 20    // 工具箱距离顶部的距离
    // },
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
        // console.log(_this.item_data_human,"item_data_human")
        _this.item_data_human.forEach(item=>{
          const value = parseFloat(_this.profile[0][item]);
          const formattedValue = value.toExponential(6);
          // console.log(formattedValue,"formattedValue")
          option.series[0].data.push(formattedValue);
        })
        myChart1.setOption(option);
        window.addEventListener('resize', myChart1.resize);
        
      },
      drawLine2(){
        // console.log("调用dramLine2");
        
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

<style>
.title {
  text-align: center;
  font-size: 1.5em;
  line-height: 40px;
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
  filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#e6f0ef', endColorstr='#b4ede7',GradientType=1 );

}
.files {
  width: 70%;
  margin: 0 auto;
} 
.content {
  display: flex;
  flex-direction: column;
  text-align: left;
  padding: 20px;
  border: 1px solid rgb(115, 200, 200);
  border-radius: 10px;
  font-family:"Avenir", Helvetica, Arial, sans-serif;
  
}
span {
  display:inline-block;
  /* width:100%;  */
  word-wrap:break-word; 
  word-break: break-all; 
  white-space:normal ; 
  font-family:"Avenir", Helvetica, Arial, sans-serif;
  font-size:15px;
} 
.newlist {
  position: relative;
  margin: 0 auto;
  width: 70%;
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
.img_style{

  height: 45px; 
  width: auto; 
  vertical-align: middle; 
  position: absolute;
  left: 0;
}
.top{
    border-radius: 10px;
    background: rgb(115, 200, 200);
    padding: 10px;
    height: 40px;
    line-height: 40px;
    color: #e6f0ef;
    text-align:left
}
.open_style{
  height:18px;
  width:18px;
}
.hand:hover{
  color:#1ee3cf;
  cursor:pointer
}
.el-form-item{
  font-size:16px;
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

</style>