<template>
    <div>
        <el-row class="title" style="color: #606060;">
          <img
          src="../../public/assets/img/back.png"
          class="img_style"
          @click="toUrl()"
         />
            <p> Detail information of  {{ dataList.UID }}</p>

        </el-row>
       
        <div class="files">
          <h3 class="top">Gene information</h3>
          <div class="content" style="height:40%">
            <el-form label-position="left" inline class="demo-table-expand" >
              <el-form-item label="Gene UID:">
                <span>{{dataList.UID }}</span>
              </el-form-item>
              <el-form-item label="Symbol:">
                <span>{{ dataList.gene_name }}</span>
              </el-form-item>
              <!-- <el-form-item label="NONCODE ID:">
                <span>{{ dataList.Noncode_id }}</span> 
              </el-form-item> -->
              <el-form-item label="Organism:" >
                <span>{{ dataList.Organism }}</span>
              </el-form-item>
              <el-form-item label="Position:">
                <span v-if="dataList.Organism === 'Human'">{{ chr ? chr + ": " + start + "-" + end + "," + strand + "(hg38)" : "N.A."}} </span>
                <span v-else>{{ chr ? chr + ": " + start + "-" + end + "," + strand + "(mm10)" : "N.A."}}</span>
              </el-form-item>
              <el-form-item label="Lncbook Gene ID:">
                <span @click="toUrl_Lncbook(dataList.Lncbook_id)" class="hand">{{ dataList.Lncbook_id }}</span>
              </el-form-item> 
              <el-form-item label="NONCODE Gene ID:">
                <span @click="toUrl_NONCODE(dataList.Noncode_id)" class="hand">{{ dataList.Noncode_id }}</span>
              </el-form-item>
              
              <el-form-item label="NCBI Gene ID:">
                
                <span @click="toUrl_NCBI(dataList.NCBI_id)" class="hand">{{dataList.NCBI_id}}</span>
                
              </el-form-item>

              <el-form-item label="Alias:">
                <span>{{ dataList.Alias}}</span>
              </el-form-item>
              <el-form-item label="Validity:" style="width:70%">
                <el-tag v-if="dataList.vitro === 1" size="small" type="info" effect="plain" style="margin-right: 8px;" >CRISPR</el-tag>
                <el-tag v-if="dataList.vivo === 1 ||dataList.cancer_related > 0" size="small" type="info" effect="light" style="margin-right: 8px;">Literature</el-tag>
                <el-tag v-if="dataList.disease_related === 1" size="small" type="info" effect="dark" style="margin-right: 8px;">Predicted</el-tag>
              </el-form-item>
              <el-form-item label="Literature Reason:" style="width:70%">
                <span>{{ dataList.reason }}</span>
              </el-form-item>

              <el-form-item label="Gene Ontology Annotations:" style="width:70%">
                <span>{{ dataList.Go_annotation }}</span>
              </el-form-item>
              <!-- <el-form-item label="Sequence:">
                <span>{{ dataList.Sequence }}</span>
              </el-form-item> -->
              <el-form-item label="CRISPR Experimental Records:"></el-form-item>
              <el-table :data="expData" border style="width: 80%;">
                <el-table-column label = "Target" prop="target_id" width="150"></el-table-column>
                <el-table-column label = "CRISPR Type" prop="exp_type" width="150"></el-table-column>
                <el-table-column label = "Exp Score" prop="exp_score" width="150"></el-table-column>
                <el-table-column label = "Role" prop="role" width="150"></el-table-column>
                <el-table-column label = "Cell Line" prop="cell_line" width="150"></el-table-column>
                <el-table-column label = "PubMed ID" prop="PMID" ></el-table-column>
              </el-table>
            </el-form>
          </div>

        </div>
        <div class="files">
          <h3 class="top">Transcripts In Gene</h3>
          <div class="content" style="height:600px">
            <div class="tabletitle" v-if="id==1">
                <el-row>
                    <el-col :span="4" :offset="10">
                        Transcript ID 
                    </el-col>
                </el-row>
            </div>
            <el-table
            :header-cell-style="{background:'#eef1f6',color:'#606266'}"
            height="600"
            :data="itemData"
            empty-text="N.A."
            border>

            <el-table-column
            label="TRANSCRIPT ID"           
            >
                <template #default="props"   >
                    <span  class="hand" @click="toVisual(props.row)">{{ props.row.transcript_id}}
                    <img
                    src="../../public/assets/img/jump.png"
                    style="width:10px; height:10px"
                    @click="toVisual(props.row)"
                    />
                    </span>
                </template>

            </el-table-column>

            </el-table>
  
          </div>
        </div>
        <div class="files">
          <h3 class="top">Diease Related</h3>
          <div class="content" style="height:40%">
            <el-table 
            :data="diseaseData" 
            height="600"
            :header-cell-style="{background:'#eef1f6',color:'#606266'}"
            empty-text="N.A."
            border>
              <el-table-column label = "Gene UID" width="120">{{ UID }}</el-table-column>
              <el-table-column label = "Variant ID" prop="variation_id" width="120"></el-table-column>
              <el-table-column label = "chr" prop="chr" width="60"></el-table-column>
              <el-table-column label = "start site" prop="variant_start" width="100"></el-table-column>
              <el-table-column label = "end site" prop="variant_end" width="100"></el-table-column>
              <el-table-column label = "Variant Type" prop="variant_type" ></el-table-column>
              <el-table-column label = "Clinical significance" prop="clinical_significance" ></el-table-column>
              <el-table-column label = "Source" width="100" >ClinVar</el-table-column>
              <!-- expand -->
              <el-table-column type="expand" label="Details" width="100">
                <template #default="props">
                  <el-form label-position="left" inline class="demo-table-expand" >
                    <el-form-item label="Reference allele: ">
                      <span>{{ props.row.reference_allele}}</span>
                    </el-form-item>
                    <el-form-item label="Alternate allele: ">
                      <span>{{ props.row.alternate_allele}}</span>
                    </el-form-item>
                    <el-form-item label="Phenotype">
                      <span id="span_style">{{ props.row.phenotype}}</span>
                    </el-form-item>
                  </el-form>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </div>  
    </div>
</template>

<script>
import axios from "axios";
export default{
    data(){
        return{
            dataList:{},
            itemData:[],
            diseaseData:[],
            expData:[],
            DNAid:"NONHSAG000195.3",
            detailData:{},
            chr:"",
            start:"",
            end:"",
            strand:"",
            tempPage:"",
            UID:"",


        }
    },
    mounted(){
        window.scrollTo(0, 0);
        this.tempPage = this.$route.query.page
        // console.log("标记Gene页面上个页面从哪里来",this.$route.params)
        if(this.tempPage == "Browse"){          
          this.dataList = JSON.parse(sessionStorage.getItem("dataBrowse"));
          console.log(this.dataList,"browse")
        }
        if(this.tempPage == "Search"){          
          this.dataList = JSON.parse(sessionStorage.getItem("dataSearch"));
          console.log(this.dataList,"search")
        }
        if(this.tempPage == "Blast"){          
          this.dataList.UID = JSON.parse(sessionStorage.getItem("dataBlast")).UID;
          console.log(this.dataList,"blast")
        }
        // console.log(this.dataList,'test');
        this.UID = this.dataList.UID;
        // this.DNAid = this.dataList.NONCODEId;
        


        axios.post("api/property/transcript",{    
            UID:this.UID
        }).then(respond =>{
            console.log(respond.data);
            this.itemData=respond.data;
        });
        axios.post("api/property/gene",{
            UID:this.UID
        }).then(respond =>{
            console.log(respond.data,"detail")
            this.dataList=respond.data[0];
            const data = respond.data;
            // console.log(data)
            this.chr = this.dataList.chr;
            const strand = this.dataList.strand;
            this.strand = strand == '+' ? "forward" : "reverse";
            this.start = Math.min(...data.map(item => item.start));
            this.end = Math.max(...data.map(item => item.end));
            // console.log(this.start,this.end)
        });

        axios.post("api/property/experiment",{
            UID:this.UID
        }).then(respond =>{
            // console.log(respond.data);
            this.expData=respond.data;
        });

        // disease related
        axios.post("api/property/diseaseMap",{
            UID:this.UID
        }).then(respond =>{
            console.log(respond.data);
            this.diseaseData=respond.data.disease;
        });
    },
    methods:{
      toUrl(){
        this.$router.push({
          name:this.tempPage,

        })
      },
//    这是传的什么参数
      toVisual(data){
        // console.log(JSON.stringify(data))
        sessionStorage.setItem('dataGene', JSON.stringify(data));
        this.$router.push({
          name:'Visual',
          params:data,
          query:{page:this.tempPage}
        })
      },

      toUrl_NCBI(data){
         window.location.href = "https://www.ncbi.nlm.nih.gov/gene/"+data

      },
      toUrl_NONCODE(data){
         window.location.href = "http://www.noncode.org/show_gene.php?id="+data.split(".")[0]+"&version="+data.split(".")[1]+"&utd=1#"
      },
      toUrl_Lncbook(data){
         window.location.href = "https://ngdc.cncb.ac.cn/lncbook/gene?geneid="+data
      }
    }

}

</script>

<style >
.hand:hover{
  color:#1ee3cf;
  cursor:pointer
}
.el-form-item__label{
  font-weight: bold;
}
</style>