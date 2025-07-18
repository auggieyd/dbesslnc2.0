<template>
  <div>
    <el-row class="title" style="color: #606060;">
      <img
        src="../../public/assets/img/help.png"
        style="height: 45px; width: auto;  vertical-align: middle; margin-right: 20px;"
      />
      Help
    </el-row>
    <div class="perspective">
      <h3>Tutorial</h3>
      <el-collapse v-model="activeName" accordion class="content">
        <el-collapse-item title="1. Overview" name="1">
          <p>
           Essential lncRNAs are important for fundamental cellular processes including 
           gene expression regulation and signal pathways,even concerned with the progression
            of the diseases or tumors.Here,we developed a database named dbEssLnc2.0 
            (<b><a href="https://esslnc.pufengdu.org/v2/">https://esslnc.pufengdu.org/v2/</a></b>),which manually 
            collects and collates essential lncRNAs information from existing databases and published 
            literature. Currently, the dbEssLnc2.0 database contains <b>6315</b> essential lncRNAs , 
            and the data will be continuously added and updated.
          </p>
          <img width="400" alt="browse help" src="../../public/assets/img/help/work.svg" />
        </el-collapse-item>

        <el-collapse-item title="2. Browse help" name="2">
          <p>
            <strong>(1).</strong> Users can browse information of essential lncRNAs 
            and their original references. The navigation bar on the left side shows 
            all the contents users can browse in the 'Browse' page. It takes some time to
            load data when opening the page.
          </p>
          <p>
            <strong>(2).</strong> Users can click on the Gene UID to navigate to the gene details page.
          </p>
          <p>
            <strong>(3).</strong> The NCBI_gene_Id and PubMed  in the table can directly go to the NCBI
            website to read gene and article information.
          </p>
          <img alt="browse help" src="../../public/assets/img/help/bhelp.png" />
        </el-collapse-item>
        <el-collapse-item title="3. Gene help" name="3">
          <p>
            <strong>(1).</strong> Users can click lncRNA gene name in "Browse" or "Search" page, then page will jump to this "Gene" page. The "Gene"
            page show detail information of gene, such as gene symbol, LncBook gene id,NONCODE gene id, position, NCBI gene id ,aliase,the reason to be essential,organism, 
            gene ontology annotations and CRISPR experimental records . Users click "LncBook Gene ID/NONCODE Gene ID" can link to LncBook/NONCODE database, click "NCBI Gene ID" can link to NCBI website.
          </p>
          <img alt="gene help" src="../../public/assets/img/help/ghelp.png" />

          <p>
            <strong>(2).</strong> Gene page also show  all transcript id of this gene in in their original sources.Users click "transcript id" can link to
            "Visual" page.
          </p>
          <img alt="gene help" src="../../public/assets/img/help/thelp.png" />

        </el-collapse-item>

        <el-collapse-item title="4. Visual help" name="4">
          <p>
            <strong>(1).</strong> Users click lncRNA gene name, page will jump to this 'visual' page. The 'visual'
            page show detail information of lncRNA gene, such as name, NONCODE id, NCBI gene id ,the reason to be 
            essential,organsim, gene ontology annotations and gene sequence.
          </p>
          <img alt="visual help" src="../../public/assets/img/help/tdhelp.png" />
          <p>
            <strong>(2).</strong>This part show the expression profile data of lncRNA. The mouse expression
            profile data included six tissues.
          </p>
          <img alt="visual help" src="../../public/assets/img/help/visual2.png" />
          <p>
            <strong>(3).</strong>This part show the expression profile data of lncRNA. The human expression 
            profile data included 24 tissues.
          </p>
          <img alt="visual help" src="../../public/assets/img/help/vhelp.png" />
        </el-collapse-item>

        <el-collapse-item title="5. Descriptions about 'Search' page and Fuzzy search" name="5">
          <p>
            <strong>(1).</strong> The picture below is an introduction to the
            'Search' page. A dropdown menu will be displayed if the content of
            the search box matches the first few letters of the names of
            essential lncRNAs.
          </p>
          <p>
            <strong>(2).</strong>The query box supports wildcard queries using '_' and '%'.
             Where '_' can match any single character, and '%' matches any number of characters.
          </p>
          <img alt="search help" src="../../public/assets/img/help/shelp.png" />
          
          <p>
            <strong>(3).</strong> Users click gene UID ,page will link to "Gene" page.
          </p>
           <img alt="search help" src="../../public/assets/img/help/shelp2.png" />
        </el-collapse-item>
        
        <el-collapse-item title="6. Blast help" name="6">
          <p>
            <strong>(1).</strong>
            In the 'Blast' page, the user can enter the lncRNA sequence in FASTA format for  
            alignment with sequence stored in the database，and the results of sequence 
            alignment will  be display below.
             Enter lncRNA sequence or click 'Example' to use template lncRNA sequence.
          </p>
          <p>
            <strong>(2).</strong>
            Set e-value and word size,then click 'Blast' button to doing sequence alignment, the result will be shown in following table.
          </p>
          <p>
            <strong>(3).</strong>
            For example, Users input the sequence of MEG3 in mouse,will see homologous gene meg3 in mouse.
          </p>
          <img alt="batch convert help" src="../../public/assets/img/help/bhelp1.png" />
          <p>
            <strong>(4).</strong>
            Clicking the expand button allows you to view detailed information, and clicking the Gene UID directs you to the gene detail page.
          </p>
          <img alt="batch convert help" src="../../public/assets/img/help/bhelp2.png" />
        </el-collapse-item>
        <el-collapse-item title="7. Download help" name="7">
          <p>
            <strong>(1).</strong> Users can download all data and source code of dbEssLnc2.0 database.
          </p>
          <img alt="download help" src="../../public/assets/img/help/download.png" />
        </el-collapse-item>
      </el-collapse>
   </div>
    <div class="perspective">
      <h3>Statistics</h3>
      <div class="setborder">
        <p>Currently,this dbEssLnc2.0 database include <b>6315</b> essential lncRNAs.</p>
        <p>Sorted by organsim, there are <b>6283</b> essential lncRNAs belonging to human and <b>34</b> essential lncRNAs belonging to mouse.</p>
        <p>Sorted by reason, there are <b>41</b> essential lncRNAs belonging to general
          , <b>88</b> essential lncRNAs belonging to tumor suppressor 
          and <b>117</b> essential lncRNAs belonging to oncogene, <b>1161</b> essential lncRNAs belonging to cell viability and <b>5059</b> essential lncRNAs belonging to disease-related.</p>

        <div id ="first"></div>
        <div id ="second"></div>
        

      </div>
    </div>

    <div class="perspective">
      <h3>Contact</h3>
      <div class="setborder">
        <p>
          For any suggestions, technical issues, data depositions and error
          reports, please contact Dr. Pu-Feng Du by email (<a
            href="mailto:pdu@tju.edu.cn"
            >pdu@tju.edu.cn</a
          >).
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import echarts from "echarts"
export default {
  data() {
    return {
      activeName: ["1"]
    };
  },
  mounted () {
    this.drawLine()
  },
  methods: {
    drawLine (){
      var chartDom1 = document.getElementById('first');
      var myFirstChart = echarts.init(chartDom1);

      var chartDom2 = document.getElementById('second');
      var mySecondChart = echarts.init(chartDom2);
      var colors=['#D3E397','#d9d9f3','#AEC6CF','#B2D8BB','#96ceb4','#D9CDB8'];

      var option1 = {
      title: {
        text: 'Group by Organism',
        left: 'center'
      },
      xAxis: {
        type: 'category',
        data: ['Human', 'Mouse']
      },
      yAxis: {
        type: 'value'
      },
      tooltip: {
      trigger: 'item'
      },
      series: [
        {
        data: [{value:6281,name:'Human'},{value:34,name:'Mouse'}],
        type: 'bar',
        itemStyle:{
          normal:{
            color:function (params) {
              return colors[params.dataIndex];
            },
              label:{
                show:true,
                position:'top',
                color:'black'
              }
          }
        },
        barWidth:'40%'
        }
      ]
    };
    var option2 = {

    title: {
      text: 'Group by Essential role',
      left: 'center'
    },
    xAxis: {
      type: 'category',
      data: ['general', 'tumor suppressor ', 'oncogene','cell viability','disease-related'],
      axisLabel: {
            // rotate: 30, // 旋转30度
            interval: 0, // 显示所有标签
   
        }
    },
    yAxis: {
      type: 'value'
    },
    tooltip: {
      trigger: 'item'
    },
    series: [
      {
        data: [41,88,117,1161,5059],
        type: 'bar',
        itemStyle:{
          normal:{
              color:function (params) {
              return colors[params.dataIndex+2];
            },
            label:{
                show:true,
                position:'top',
                color:'black'
              }
          }        
        },
        barWidth:'40%'
      }
    ]
  };

    myFirstChart.setOption(option1);
    mySecondChart.setOption(option2);


    }
  }
};
</script>
<style scoped >
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

.content {
  /* width: 90%; */
  margin: 10px auto;
  padding: 2px;
  border: 2px solid #b4ede7;
  border-radius: 10px;
  background-color: #b4ede7;
}

.content img {
  width: 80%;
  height: auto;
  margin-left: 5vw;
}

:deep(.el-collapse-item__header) {
  font-size: 16px;
  padding-left: 20px;
}

:deep( .el-collapse-item__content ){
  border-top: 1px solid #b4ede7;
}

p {
  font-size: 16px;
  line-height: 1.5em;
  text-align: justify;
  padding: 0 30px;
}

.perspective {
  width: 90%;
  margin: 0 auto;
}

.setborder {
  border: 2px solid #b4ede7;
  border-radius: 10px;
}

h3 {
  text-align: left;
  padding: 10px;
  background-color: rgb(115, 200, 200);
  color: #e6f0ef;
  border-radius: 10px;
}
#first{
  width:800px;
  height:500px;
  display: inline-block;

}
#second {
    width:800px;
    height:500px;
    display: inline-block;

}
:deep(.el-collapse-item__header){
  font-weight: bold;
}

</style>
