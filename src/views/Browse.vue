<template>
  <div>
    <el-row class="title" style="color: #606060;">
      <img
        style="margin-right: 20px; height: 55px; width: 55px; vertical-align: middle;"
        src="../../public/assets/img/browse.png"
      />
      Browse all
    </el-row>
    <el-container style="height: expression(document.body.clientHeight-130px); border: 1px solid #eee">
      <!-- 侧边导航栏 -->
      <el-aside 
        width="300px"
        style="background-color: rgb(238, 241, 246); text-align:left;">
        <el-menu :default-openeds="['1']">
          <el-submenu index="1">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>General</b>
            </template>

            <el-menu-item index="1-1" >
              <!-- <a href="#vital">essential lncRNA</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#vital')">General</a>
            </el-menu-item>
          </el-submenu>

          <!-- Cell growth and proliferation -->
          <el-submenu index="2">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>Cell growth and proliferation</b>
            </template>
            <el-menu-item index="2-1" >
              <!-- <a href="#vital">essential lncRNA</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#crispr-type')">cell viability</a>
            </el-menu-item>
          </el-submenu>   
          <!-- Cancer related -->
          <el-submenu index="3">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>Cancer related</b>
            </template>

            <el-menu-item index="3-1" >
              <!-- <a href="#tumor">tumor suppressor genes</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#tumor')">Tumor suppressor</a>
            </el-menu-item>

            <el-menu-item index="3-2">
              <!-- <a href="#cancer">essential lncRNA in cancer cell</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#cancer')">Oncogene</a>
            </el-menu-item>
          </el-submenu>   
          <!-- Disease related -->
          <el-submenu index="4">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>Disease related</b>
            </template>
            <el-menu-item index="5-1" >
              <!-- <a href="#vital">essential lncRNA</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#disease-related')">Diease related</a>
            </el-menu-item>
          </el-submenu>
          <!-- Organism -->
          <el-submenu index="5">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>Organism</b>
            </template>

            <el-menu-item index="4-1" >
              <!-- <a href="#vital">essential lncRNA</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#ren')">Human</a>
            </el-menu-item>

            <el-menu-item index="4-2" >
              <!-- <a href="#tumor">tumor suppressor genes</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#xiaoshu')">Mouse</a>
            </el-menu-item>
          </el-submenu>

        </el-menu>

      </el-aside>
      <!-- 显示表格 -->
      <el-container >
        <el-main>

        <!-- show vital -->
          <div>
            <!-- <a name="vital"></a> -->
            <h3 id="vital">In Vivo</h3>
            <el-table
            :data = "vital"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >

            <el-table-column label="Gene UID" prop="UID" width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>

            <el-table-column 
              label="Symbol" 
              prop="gene_name" 
              width="150">
            </el-table-column>

            <el-table-column prop="NCBI_id" label="NCBI Gene ID" width="150">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>

            <el-table-column
              label="Organism"
              prop="Organism"
              width="150">
            </el-table-column>

            <el-table-column label="Validity" prop="evidence_type" width = "200">
              <template v-slot="scope">
                <!-- 如果 evidence_type 为 1，显示 Literature 标签 -->
                <el-tag v-if="scope.row.evidence_type === 1" type="info" effect="light">
                  Literature
                </el-tag>
              </template>
            </el-table-column> 
            
            <el-table-column
              label="Essential role"
              prop="Role"
              width="150">
            </el-table-column>

            <el-table-column prop="PubMedID" label="PubMedID" width="150">
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>
                        <!-- 扩展部分 -->
            <!-- <el-table-column type="expand" label="Details" width="200">
              <template #default="props">
                <el-form label-position="left" inline class="demo-table-expand" >
                  <el-form-item label="NONCODE Gene ID:">
                    <span @click="toUrl_NONCODE(props.row.NONCODEId)" class="hand">{{ props.row.NONCODEId}}</span>
                  </el-form-item>
                  <el-form-item label="Aliase:">
                    <span>{{ props.row.Aliases}}</span>
                  </el-form-item>
                  <el-form-item label="Gene Ontology Annotations:">
                    <span id="span_style">{{props.row.Gene_Ontology_Annotations }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column> -->


            </el-table>    
          </div>
        <!-- show crispr cell -->
          <div>
            <h3 id="crispr-type">Cell growth and proliferation</h3>
            <!-- select Filter -->
            <!-- <div class="select-container">
              <el-select v-model="typeValue" placeholder="Select Crispr type" style="width: 200px;">
                <el-option
                  v-for="item in optionsType"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              <el-select v-model="lineValue" placeholder="Select Cell lines">
                <el-option
                  v-for="item in optionsCellLine"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              <el-button type="primary" style="font-weight: bold;">Filter</el-button>
            </div> -->
            <el-table
            :data = "cellGrowth"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
              <el-table-column
              label="Gene UID"
              prop="UID"
              width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
              </el-table-column>

              <el-table-column
              label="Symbol"
              prop="gene_name"
              width="150">
              </el-table-column>
              <el-table-column
              label="NCBI Gene ID"
              prop="NCBI_id"
              width="150">
              </el-table-column>
              <el-table-column
              label="Organism"
              prop="Organism"
              width="150">
              </el-table-column>
              <el-table-column
              label="Validity"
              prop="evidence_type"
              width="200">
              <template v-slot="scope">
                <el-tag size = "small" v-if="scope.row.evidence_type === 0" type="info" effect="plain">
                  CRISPR
                </el-tag>
                <!-- 如果 evidence_type 为 1，显示 Literature 标签 -->
                <el-tag size = "small" v-if="scope.row.evidence_type === 1" type="info" effect="light">
                  Literature
                </el-tag>
                <!-- 如果 evidence_type 为 2，显示两个标签 -->
                <div v-if="scope.row.evidence_type === 2">
                  <el-tag size = "small" type="info" effect="plain">CRISPR</el-tag>
                  <el-tag size = "small" type="info" effect="light">Literature</el-tag>
                </div>
              </template>
              </el-table-column>
              <el-table-column
              label="Essential role"
              prop = "role"
              width="150">
              </el-table-column>
              <el-table-column
              label="PubMedID"
              prop="PMID"
              width="150">
              </el-table-column>
            </el-table>
            <el-pagination
              class="pagination"
              background 
              v-model:current-page="currentPageCell"
              v-model:page-size="pageSizeCell"
              @current-change="handleCellChange"
              layout="prev, pager, next, jumper"
              :total="cellTotal"></el-pagination>
          </div> 
        <!-- show tumor -->
          <div>
            <!-- <a name="tumor"></a> -->
            <h3 id="tumor">Tumor suppressor</h3>
            <el-table
            :data = "tumor"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
            <el-table-column label="Gene UID" prop="UID" width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              width="150">
            </el-table-column>

            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" width="150">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>

            <el-table-column
              label="Organism"
              prop="Organism"
              width="150">
            </el-table-column>
            <el-table-column label="Validity" prop="evidence_type" width = "200">
              <template v-slot="scope">
                <el-tag size = "small" v-if="scope.row.evidence_type === 0" type="info" effect="plain">
                  CRISPR
                </el-tag>
                <!-- 如果 evidence_type 为 1，显示 Literature 标签 -->
                <el-tag v-if="scope.row.evidence_type === 1" type="info" effect="light">
                  Literature
                </el-tag>
                <!-- 如果 evidence_type 为 2，显示两个标签 -->
                <div v-if="scope.row.evidence_type === 2">
                  <el-tag type="info" effect="plain">CRISPR</el-tag>
                  <el-tag type="info" effect="light">Literature</el-tag>
                </div>
              </template>
            </el-table-column> 

            <el-table-column
              label="Essential role"
              prop="Role"
              width="150">
            </el-table-column>

            <!-- <el-table-column
              label="Ess Reason Description"
              prop="Reason">
            </el-table-column> -->
            
            <el-table-column prop="PubMedID" label="PubMedID" width="150">
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>
            <!-- expand -->
            <!-- <el-table-column type="expand" label="Details" width="100">
              <template #default="props">
                <el-form label-position="left" inline class="demo-table-expand" >

                  <el-form-item label="NONCODE Gene ID:">
                    <span @click="toUrl_NONCODE(props.row.NONCODEId)" class="hand">{{ props.row.NONCODEId}}</span>
                  </el-form-item>

                  <el-form-item label="Aliase:">
                    <span>{{ props.row.Aliases}}</span>
                  </el-form-item>
                  <el-form-item label="Gene Ontology Annotations:">
                    <span id="span_style">{{ props.row.Gene_Ontology_Annotations }}</span>
                  </el-form-item>

                </el-form>
              </template>
            </el-table-column> -->

            </el-table>    
          </div>
        <!-- show cancer -->
          <div>
            <!-- <a name="cancer"></a> -->
            <h3 id = "cancer">Oncogene</h3>
            <el-table
            :data = "cancer"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
            <el-table-column
              label="Gene UID"
              prop="UID"
              width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              width="150">
            </el-table-column>
            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" width="150">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>
            <el-table-column
              label="Organism"
              prop="Organism"
              width="150">
            </el-table-column>
            <el-table-column label="Validity" prop="evidence_type" width = "200">
              <template v-slot="scope">
                <el-tag v-if="scope.row.evidence_type === 0" type="info" effect="plain">
                  CRISPR
                </el-tag>
                <!-- 如果 evidence_type 为 1，显示 Literature 标签 -->
                <el-tag v-if="scope.row.evidence_type === 1" type="info" effect="light">
                  Literature
                </el-tag>
                <!-- 如果 evidence_type 为 2，显示两个标签 -->
                <div v-if="scope.row.evidence_type === 2">
                  <el-tag type="info" effect="plain">CRISPR</el-tag>
                  <el-tag type="info" effect="light">Literature</el-tag>
                </div>
              </template>
            </el-table-column> 
            <el-table-column
              label="Essential role"
              prop="Role"
              width="150">
            </el-table-column>

            <!-- <el-table-column
              label="Ess Reason Description"
              prop="Reason">
            </el-table-column> -->

            <el-table-column prop="PubMedID" label="PubMedID" width="100">
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>
            <!-- expand -->
            <!-- <el-table-column type="expand" label="Details" width="100">
              <template #default="props">
                <el-form label-position="left" inline class="demo-table-expand" >
                  <el-form-item label="NONCODE Gene ID:">
                    <span @click="toUrl_NONCODE(props.row.NONCODEId)" class="hand">{{ props.row.NONCODEId}}</span>
                  </el-form-item>
                  <el-form-item label="Aliase:">
                    <span>{{ props.row.Aliases }}</span>
                  </el-form-item>
                  <el-form-item label="Gene Ontology Annotations:">
                    <span id="span_style">{{ props.row.Gene_Ontology_Annotations }}</span>
                  </el-form-item>
                </el-form>
              </template>
            </el-table-column> -->

            </el-table>    
          </div>
        <!-- show disease -->
          <div>
            <h3 id = "disease-related">Disease related</h3>
            <el-table
            :data = "disease"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
            <el-table-column
              label="Gene UID"
              prop="UID"
              width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column> 
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              width="150">
            </el-table-column>
            <el-table-column prop="NCBI_id" label="NCBI Gene ID" width="150">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>
            <el-table-column
              label="Organism"
              prop="Organism"
              width="150">
              Human
            </el-table-column>
            <el-table-column label="Validity" prop="evidence_type">
              <template v-slot="scope">
                <div  v-if="scope.row.evidence_type === 0">
                  <el-tag size="small" type="info" effect="plain">CRISPR</el-tag>
                  <el-tag size="small" type="info" effect="dark">Predicted</el-tag>
                </div>
                <div  v-if="scope.row.evidence_type === 1">
                  <el-tag size="small" type="info" effect="light">Literature</el-tag>
                  <el-tag size="small" type="info" effect="dark">Predicted</el-tag>
                </div>
                <div  v-if="scope.row.evidence_type === 2">
                  <el-tag size="small" type="info" effect="plain">CRISPR</el-tag>
                  <el-tag size="small" type="info" effect="light">Literature</el-tag>
                  <el-tag size="small" type="info" effect="dark">Predicted</el-tag>
                </div>
                <div  v-if="scope.row.evidence_type === 3">
                  <el-tag size="small" type="info" effect="dark">Predicted</el-tag>
                </div>

              </template>
            </el-table-column> 
            <el-table-column
              label="Essential role"
              width="180">
              Pathogenic
            </el-table-column>
            <el-table-column
              label="Source"
              width="150">
              ClinVar
            </el-table-column>
            </el-table>    
            <el-pagination
              class="pagination"
              background 
              v-model:current-page="currentPageDisease"
              v-model:page-size="pageSizeCell"
              @current-change="handleDiseaseChange"
              layout="prev, pager, next, jumper"
              :total="diseaseTotal"></el-pagination>
          </div>
        <!-- human -->
          <div>
         
            <h3 id = "ren">Human</h3>
            <el-table
            :data = "ren"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
            <el-table-column
              label="Name"
              prop="Name"
              width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.Name}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" width="150">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_gene_Id" target="_black">
                {{scope.row.NCBI_gene_Id}}
              </a>
              </template>
            </el-table-column>

            <el-table-column
              label="Role"
              prop="Role"
              width="140">
            </el-table-column>
            <el-table-column
              label="Detailed Reason Description"
              prop="Reason">
            </el-table-column>

            <el-table-column prop="PubMedID" label="PubMedID" width="100">
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>

            <el-table-column type="expand" label="Details" width="100">
              <template #default="props">
                <el-form label-position="left" inline class="demo-table-expand" >
                  <el-form-item label="NONCODE Gene ID:">
                    <span @click="toUrl_NONCODE(props.row.NONCODEId)" class="hand">{{ props.row.NONCODEId}}</span>
                  </el-form-item>
                  <el-form-item label="Aliase:">
                    <span>{{ props.row.Aliases }}</span>
                  </el-form-item>
                  <el-form-item label="Gene Ontology Annotations:">
                    <span id="span_style">{{ props.row.Gene_Ontology_Annotations }}</span>
                  </el-form-item>
                  <!-- <el-form-item label="Gene Sequence:" >
                    <span id="span_style">{{ props.row.fasta }}</span>
                  </el-form-item> -->
                </el-form>
            </template>
            </el-table-column>

            </el-table>    
          </div>
        <!-- mouse -->
          <div>
           
            <h3 id = "xiaoshu">Mouse</h3>
            <el-table
            :data = "xiaoshu"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
            <el-table-column
              label="Name"
              prop="Name"
              width="150">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.Name}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" width="150">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_gene_Id" target="_black">
                {{scope.row.NCBI_gene_Id}}
              </a>
              </template>
            </el-table-column>

            <el-table-column
              label="Role"
              prop="Role"
              width="140">
            </el-table-column>
            <el-table-column
              label="Detailed Reason Description"
              prop="Reason">
            </el-table-column>

            <el-table-column prop="PubMedID" label="PubMedID" width="100">
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>

            <el-table-column type="expand" label="Details" width="100">
              <template #default="props">
                <el-form label-position="left" inline class="demo-table-expand" >
                  <el-form-item label="NONCODE Gene ID:">
                    <span @click="toUrl_NONCODE(props.row.NONCODEId)" class="hand">{{ props.row.NONCODEId}}</span>
                  </el-form-item>
                  <el-form-item label="Aliase:">
                    <span>{{ props.row.Aliases }}</span>
                  </el-form-item>
                  <el-form-item label="Gene Ontology Annotations:">
                    <span id="span_style">{{ props.row.Gene_Ontology_Annotations }}</span>
                  </el-form-item>
            
                </el-form>
            </template>
            </el-table-column>

            </el-table>    
          </div>
        <!-- show cell line -->
        <!-- <div>
            <h3 id="cell-line">cell line</h3>
            <el-table
            :data = "Hela"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >
            <el-table-column
              label="gene_id"
              prop="gene_id"
              width="100">
            </el-table-column>
            <el-table-column
              label="exp_type"
              prop="exp_type"
              width="150">
            </el-table-column>
            <el-table-column
              label="cell_line"
              prop="cell_line"
              width="150">
            </el-table-column>
            <el-table-column
              label="exp_score"
              prop="exp_score"
              width="150">
            </el-table-column>
            <el-table-column
              label="role"
              prop="role"
              width="150">
            </el-table-column>
            
            </el-table>
        </div>  -->


        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import { ElLoading } from 'element-plus'
import { options } from "less";

export default{
  data () {
    return {
      url:"https://www.ncbi.nlm.nih.gov/pubmed/?term=",
      urlNCBI:"https://www.ncbi.nlm.nih.gov/gene/",
      cellTotal:0,
      diseaseTotal:0,
      vital:[],
      tumor:[],
      cancer:[],
      disease:[],
      ren:[],
      xiaoshu:[],
      Hela:[],
      cellGrowth:[],
      ci:[],
      count:6,
      tagTypes: ['success', 'info', 'warning', 'danger'],
      typeValue: '',
      lineValue: '',
      currentPageCell: 1,
      currentPageDisease: 1,
      pageSizeCell: 10,
      optionsType: [
        {
          value: 'CRISPRi',
          label: 'CRISPRi'
        },
        {
          value: 'CRISPR-site',
          label: 'CRISPR-site'
        },
        {
          value: 'CRISPR-pair-guide',
          label: 'CRISPR-pair-guide'
        },
        {
          value: 'CRISPR-casRx',
          label: 'CRISPR-casRx'
        }
      ],
      optionsCellLine: [
        {
          value: 'HeLa',
          label: 'HeLa'
        },
        {
          value: 'K562',
          label: 'K562'
        },
        {
          value: 'Huh7.5',
          label: 'Huh7.5'
        },
        {
          value: 'GM12878',
          label: 'GM12878'
        },
        {
          value: 'HEK293T',
          label: 'HEK293T'
        },
        {
          value: 'U87',
          label: 'U87'
        },
        {
          value: 'IPSC',
          label: 'IPSC'
        },
        {
          value: 'MCF7',
          label: 'MCF7'
        },
        {
          value: 'MDA-MB-231',
          label: 'MDA-MB-231'
        },
        {
          value: 'LN18',
          label: 'LN18'
        },
        {
          value: 'LN229',
          label: 'LN229'
        },
        {
          value: 'KP4',
          label: 'KP4'
        },
        {
          value: 'A549',
          label: 'A549'
        },
        {
          value: 'MIAPACA2',
          label: 'MIAPACA2'
        },
        {
          value: 'NICH460',
          label: 'NICH460'
        }
      ],
      colorMap: {
        'hela': '#8B0000', // Dark Red
        'K562': '#006400', // Dark Green
        'Huh7.5': '#00008B', // Dark Blue
        'GM12878': '#8B008B', // Dark Magenta
        'HEK293T': '#4B0082', // Indigo
        'U87': '#2F4F4F', // Dark Slate Gray
        'IPSC': '#FF4500', // Orange Red
        'MCF7': '#2E8B57', // Sea Green
        'MDA-MB-231': '#4682B4', // Steel Blue
        'LN18': '#D2691E', // Chocolate
        'LN229': '#9ACD32', // Yellow Green
        'KP4': '#DAA520', // Goldenrod
        'A549': '#B22222', // Firebrick
        'MIAPACA2': '#8B4513', // Saddle Brown
        'NICH460': '#5F9EA0' // Cadet Blue
      }

      // vitalShow:1
      // fullscreenLoading: false
    }
  },
  mounted () {
      var _this =this;
      ElLoading.service({
        fullscreen:true,
        text:"Loading...",
        background:"rgba(0,0,0,0.7)"
      });

//show vital table data 
      axios.post("api/property/vital").then(respond =>{
      _this.vital = respond.data;
      // console.log(_this.vital);
      _this.count-- ;
      _this.LoadingClose();
      });
//show tumor table data
      axios.post("api/property/tumor").then(respond =>{
      _this.tumor = respond.data;
      _this.count-- ;
      _this.LoadingClose();
      //console.log("tumor")

      });
//show cancer table data
      axios.post("api/property/cancer").then(respond =>{
      _this.cancer = respond.data;
      _this.count-- ;
      _this.LoadingClose();
      //console.log("cancer")

      });
      axios.post("api/property/selectHuman").then(respond =>{
      _this.ren = respond.data;
      // console.log(_this.ren);
      _this.count-- ;
      _this.LoadingClose();
      //console.log("cancer")

      });
      axios.post("api/property/selectMouse").then(respond =>{
        
      _this.xiaoshu = respond.data;
      // console.log(_this.xiaoshu);
      _this.count-- ;
      _this.LoadingClose();
      //console.log("cancer")

      })
// show Celluar table data
      axios.post("api/property/cellgrowth",{
        page:_this.currentPageCell,
        pageSize:_this.pageSizeCell
      }).then(respond =>{
        // console.log(respond.data);
        _this.cellGrowth = respond.data.items;
        _this.cellTotal = respond.data.total;
      // console.log(_this.cellGrowth);

        _this.count-- ;
        _this.LoadingClose();
      //console.log("cancer")
      })
// show disease table data
      axios.post("api/property/diseaseRelated",{
        page:_this.currentPageDisease,
        pageSize:_this.pageSizeCell
      }).then(respond =>{
      _this.disease = respond.data.items;
      _this.diseaseTotal = respond.data.total;
      // console.log(_this.cancer);
      _this.count-- ;
      _this.LoadingClose();
      //console.log("cancer")
      })
// show crispr type table data
      // axios.post("api/property/selectCi").then(respond =>{
      // _this.ci = respond.data;
      // const data = respond.data;
      // const mergedData = {};
      // data.forEach(item => {
      //   const { gene_id, cell_line, exp_score,role,exp_type } = item;

      //   // 如果 gene_id 不在 mergedData 中，初始化一个新对象
      //   if (!mergedData[gene_id]) {
      //     mergedData[gene_id] = {
      //       gene_id,
      //       cell_line: [],
      //       exp_score: [],
      //       count: 0,
      //       role,
      //       exp_type,
      //     };
      //   }

      //   // 合并 cell_line 和 exp_score，并增加 count
      //   mergedData[gene_id].cell_line.push(cell_line);
      //   mergedData[gene_id].exp_score.push(exp_score);
      //   mergedData[gene_id].count += 1;
      // });

      // // 将合并后的结果转换回数组格式，并将 cell_line 和 exp_score 用 ';' 分隔
      // const result = Object.values(mergedData).map(item => {
      //   let role;
      //   if (item.count < 2) {
      //     role = 'Cell line specific';
      //   } else if (item.count >= 2 && item.count < 6) {
      //     role = 'Common essential';
      //   } else if (item.count >= 6) {
      //     role = 'Core essential';
      //   }
      
      //   return {
      //     gene_id: item.gene_id,
      //     cell_line: item.cell_line.join(';'),
      //     exp_score: item.exp_score.join(';'),
      //     count: item.count,
      //     role: role,
      //     exp_type: item.exp_type,
      //   };
      // });

      // // 将处理后的数据赋值给 _this.ci
      // _this.ci = result;
      // console.log(_this.ci);
      //       _this.count-- ;
      //       _this.LoadingClose();
      //       //console.log("cancer")
      // })

  },
  methods: {
    // fetchCellData
    fetchCellData() {
      axios.post("api/property/cellgrowth",{
        page:this.currentPageCell,
        pageSize:this.pageSizeCell
      }).then(respond =>{
        this.cellGrowth = respond.data.items;
        this.cellTotal = respond.data.total;
      });
    },
    fetchDiseaseData() {
      axios.post("api/property/diseaseRelated",{
        page:this.currentPageDisease,
        pageSize:this.pageSizeCell
      }).then(respond =>{
        console.log(respond.data);
        this.disease = respond.data.items;
        this.diseaseTotal = respond.data.total;
      });
    },
    getTagType(index) {
      return this.tagTypes[index % this.tagTypes.length];
    },
    getColor(cell) {
      return this.colorMap[cell] || '';
    },
    LoadingClose (){
      if(this.count === 0){
        let loadingInstance = ElLoading.service({});
        this.$nextTick(() => {
       // 以服务的方式调用的 Loading 需要异步关闭
          loadingInstance.close();
        });
      }
    },
    goAnchor (selector) {
      document.querySelector(selector).scrollIntoView({
        behavior:"smooth"
      })
    },

    toUrl(data){
      // data.page = "Browse"
      sessionStorage.setItem('dataBrowse', JSON.stringify(data));
      // console.log(JSON.stringify(data));
      this.$router.push({
        name:'Gene',
        params:data,
        query:{page:"Browse"}
      })
    },

    toUrl_NONCODE(data){
      
      window.location.href = "http://www.noncode.org/show_gene.php?id="+data.split(".")[0]+"&version="+data.split(".")[1]+"&utd=1#"
    },

    handleCellChange(newPage) {
      this.currentPageCell = newPage;
      this.fetchCellData();
    },
    handleDiseaseChange(newPage) {
      console.log(newPage);
      this.currentPageDisease = newPage;
      this.fetchDiseaseData();
    }
  }
}
</script>

<style scoped>
.title {
  /* text-align: center; */
  font-size: 1.5em;
  line-height: 80px;
  justify-content: center;
  align-items: center;
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
.el-table {
  font-size: 15px;
  color: #232324;
}
.el-aside {
  color: #333;
}
.el-menu-item {
  font-size: 15px;
}

h3 {
  text-align: left;
  /* border-bottom: 2px solid; */
  /* border-bottom-color: rgb(115, 200, 200); */
  padding: 10px;
  background-color: rgb(115, 200, 200);
  color: #e6f0ef;
  border-radius: 10px;
}
a {
  color: #202122;
}
a:hover {
  color: rgb(115, 200, 200);
}

.demo-table-expand {
    font-size: 0;
}
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
 .el-form-item {
 float: left;
 clear: both;
 margin-right: 0;
 margin-bottom: 0;
 width:100%;
}
.select-container {
  /* text-align: left; */
  display: flex;
  flex-direction: row; 
  gap: 10px; 
  margin-bottom: 10px;
}
.el-select-dropdown__item{
  text-indent: 0px;
}
.tag-wrapper {
  display: flex;
}
.el-tag{
  display: inline-block;
  margin: 0.2rem;
  width: auto;
}
span {
  
  display:inline-block;
  /* width:100%; */
  word-break: break-all;
  white-space:normal ;
  font-family:"Avenir", Helvetica, Arial, sans-serif;
  font-size: 15px;
  /* font-weight:bold; */
}
#span_style{
  background:#f2f4f6;
  
}
.hand:hover{
  color:#1ee3cf;
  cursor:pointer;
  font-size:15px;
  font-family:"Avenir", Helvetica, Arial, sans-serif;
}
.pagination {
  margin-top: 5px;
  width: 80%;
  text-align: center;
}
:deep(.el-pagination.is-background .el-pager li:hover) {
  color: #389a99 !important;
}
:deep(.el-pagination.is-background .el-pager li:not(.disabled):hover) {
  color: #389a99 !important;
}
:deep(.el-pagination.is-background .el-pager li:not(.disabled).active:hover) {
  background-color: #389a99 !important;
}
:deep(.el-pagination.is-background .el-pager li:not(.disabled).active) {
  background-color: #389a99 !important;  
}
</style>
