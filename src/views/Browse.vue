<template>
  <div>
    <el-row class="title" style="color: #606060;">
      <img
        style="margin-right: 20px; height: 55px; width: 55px; vertical-align: middle;"
        src="../../public/assets/img/browse.png"
      />
      Browse all
    </el-row>
    <el-container ref="dynamicHeight" style="border: 1px solid #eee">
      
      <el-aside 
        width="18vw"
        style="background-color: rgb(238, 241, 246); text-align:left;">
        <el-menu :default-openeds="['1']">
          <!-- In vivo -->
          <el-submenu index="1">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>In vivo</b>
            </template>

            <el-menu-item index="1-1" >
              <!-- <a href="#vital">essential lncRNA</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#vital')">General</a>
            </el-menu-item>
          </el-submenu>

          <!-- Cell growth and proliferation -->
          <el-submenu index="2">
            <template v-slot:title>
              <i class="el-icon-s-grid"></i><b>In vitro</b>
            </template>
            <el-menu-item index="2-1" >
              <!-- <a href="#vital">essential lncRNA</a> -->
              <a href="javascript:void(0)" @click="goAnchor('#crispr-type')">Cell viability</a>
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
              <a href="javascript:void(0)" @click="goAnchor('#disease-related')">Disease associated</a>
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

      <el-container >
        <el-main>

        <!-- show vital -->
          <div>
            <!-- <a name="vital"></a> -->
            <h3 id="vital">General</h3>
            <el-table
            :data = "vital"
            :header-cell-style ="{background:'#eef1f6',color:'#606266'}"
            height="400"
            border
            stripe
            style="width: 100%"
            strip highlight-current-row
            >

              <el-table-column label="Gene UID" prop="UID" width="120">
                <template #default="scope">
                  <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
                </template>
              </el-table-column>

              <el-table-column 
                label="Symbol" 
                prop="gene_name" 
                width="150">
              </el-table-column>

              <el-table-column prop="NCBI_id" label="NCBI Gene ID" width="130">
                <template #default="scope">
                <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                  {{scope.row.NCBI_id}}
                </a>
                </template>
              </el-table-column>

              <el-table-column
                label="Organism"
                prop="Organism"
                width="120">
              </el-table-column>

              <el-table-column
                label="Essential role"
                prop="Role"
                width="180">
                General
              </el-table-column>
              <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>

                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
              <el-table-column prop="PubMedID" label="PubMedID" width="150">
                  <template #default="scope">
                    <a :href="url+scope.row.PMID" target="_black">
                      {{scope.row.PMID}}
                    </a>
                  </template>
              </el-table-column>    
            </el-table>    
          </div>
        <!-- show crispr cell -->
         
          <div>
            <h3 id="crispr-type">Cell viability</h3>

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
              width="120">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
              </el-table-column>

              <el-table-column
              label="Symbol"
              prop="gene_name"
              width="150">
              </el-table-column>
              <el-table-column prop="NCBI_id" label="NCBI Gene ID" width="130">
                <template #default="scope">
                <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                  {{scope.row.NCBI_id}}
                </a>
                </template>
              </el-table-column>
              <el-table-column
              label="Organism"
              prop="Organism"
              width="120">
              </el-table-column>

              <el-table-column
              label="Essential role"
              prop = "role"
              width="180">
              Cell viability
              </el-table-column>
              <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
              <el-table-column prop="PubMedID" label="PubMedID" width="150">
                  <template #default="scope">
                    <a :href="url+scope.row.PMID" target="_black">
                      {{scope.row.PMID}}
                    </a>
                  </template>
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
            <el-table-column label="Gene UID" prop="UID" width="120">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              width="150">
            </el-table-column>

            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" width="130">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>

            <el-table-column
              label="Organism"
              prop="Organism"
              width="120">
            </el-table-column>

            <el-table-column
              label="Essential role"
              prop="Role"
              width="180">
              Tumor suppressor
            </el-table-column>
            <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
            
            <el-table-column prop="PubMedID" label="PubMedID" width="150">
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>
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
              width="120">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              width="150">
            </el-table-column>
            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" width="130">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>
            <el-table-column
              label="Organism"
              prop="Organism"
              width="120">
            </el-table-column>
            
            <el-table-column
              label="Essential role"
              prop="Role"
              width="180">
              Oncogene
            </el-table-column>
            <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
            <el-table-column prop="PubMedID" label="PubMedID" >
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
            </el-table-column>

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
              width="120">
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column> 
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              width="150">
            </el-table-column>
            <el-table-column prop="NCBI_id" label="NCBI Gene ID" width="130">
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>
            <el-table-column
              label="Organism"
              prop="Organism"
              width="120">
              Human
            </el-table-column>
            
            <el-table-column
              label="Essential role"
              width="180">
              Disease-associated
            </el-table-column>
            <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
              :total="diseaseTotal">
            </el-pagination>
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
              label="Gene UID"
              prop="UID"
              >
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              >
            </el-table-column>
            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" >
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>
            <el-table-column
              label="Organism"
              prop="Organism"
              >
            </el-table-column>
            <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
              <el-table-column prop="PubMedID" label="PubMedID" >
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
              </el-table-column>
            </el-table>
            <el-pagination
              class="pagination"
              background 
              v-model:current-page="currentPageHuman"
              v-model:page-size="pageSizeCell"
              @current-change="handleHumanChange"
              layout="prev, pager, next, jumper"
              :total="humanTotal">
            </el-pagination>    
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
              label="Gene UID"
              prop="UID"
              >
              <template #default="scope">
                <span @click="toUrl(scope.row)" class="hand">{{scope.row.UID}}</span>
              </template>
            </el-table-column>
            <el-table-column
              label = "Symbol"
              prop="gene_name" 
              >
            </el-table-column>
            <el-table-column prop="NCBI_gene_Id" label="NCBI Gene ID" >
              <template #default="scope">
              <a :href="urlNCBI+scope.row.NCBI_id" target="_black">
                {{scope.row.NCBI_id}}
              </a>
              </template>
            </el-table-column>
            <el-table-column
              label="Organism"
              prop="Organism"
              >
            </el-table-column>
            <el-table-column label="vivo" prop="vivo" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vivo === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vivo !== 1" class="my-icon-close"></i>                
                </template>
              </el-table-column>
              <el-table-column label="vitro" prop="role" >
                <template #default="scope">
                   
                  <i v-show="scope.row.vitro === 1" class="my-icon-check"></i>
                  <i v-show="scope.row.vitro !== 1" class="my-icon-close"></i>    
                </template>
              </el-table-column>
              <el-table-column label="Cancer-related" prop="cancer_related" >
                <template #default="scope">
                   
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
              <el-table-column prop="PubMedID" label="PubMedID" >
                <template #default="scope">
                  <a :href="url+scope.row.PMID" target="_black">
                    {{scope.row.PMID}}
                  </a>
                </template>
              </el-table-column>
            </el-table>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import { ElLoading, ElContainer, ElAside, ElMain, ElMenu, ElSubmenu, ElMenuItem,
  ElTable, ElTableColumn, ElPagination, ElRow, ElBacktop } from 'element-plus'

export default{
  components: {
    ElRow,
    ElContainer,
    ElAside,
    ElMenu,
    ElSubmenu,
    ElMenuItem,
    ElMain,
    ElTable,
    ElTableColumn,
    ElPagination,
    ElBacktop
  },
  data () {
    return {
      url:"https://www.ncbi.nlm.nih.gov/pubmed/?term=",
      urlNCBI:"https://www.ncbi.nlm.nih.gov/gene/",
      cellTotal:0,
      diseaseTotal:0,
      humanTotal:0,
      vital:[],
      tumor:[],
      cancer:[],
      disease:[],
      ren:[],
      xiaoshu:[],
      Hela:[],
      cellGrowth:[],
      ci:[],
      count:5,
      tagTypes: ['success', 'info', 'warning', 'danger'],
      typeValue: '',
      lineValue: '',
      currentPageCell: 1,
      currentPageDisease: 1,
      currentPageHuman: 1,
      pageSizeCell: 20,
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

    }
  },
  mounted () {
      var _this =this;
      ElLoading.service({
        fullscreen:true,
        text:"Loading...",
        background:"rgba(0,0,0,0.7)"
      });
      window.addEventListener('resize', this.setDynamicHeight);

//show vital table data 
      axios.post("api/property/vital").then(respond =>{
      _this.vital = respond.data;
      _this.count-- ;
      _this.LoadingClose();
      });
//show tumor table data
      axios.post("api/property/tumor").then(respond =>{
      _this.tumor = respond.data;
      _this.count-- ;
      _this.LoadingClose();

      });
//show cancer table data
      axios.post("api/property/cancer").then(respond =>{
      _this.cancer = respond.data;
      _this.count-- ;
      _this.LoadingClose();
// show humman table data
      });
      axios.post("api/property/selectHuman",{
        page:_this.currentPageHuman,
        pageSize:20
      }).then(respond =>{
      _this.ren = respond.data.items;
      _this.humanTotal = respond.data.total;
      _this.count-- ;
      _this.LoadingClose();
      });
// show mouse table data  
      axios.post("api/property/selectMouse",{
        page:1,
        pageSize:40
      }).then(respond =>{
        
      _this.xiaoshu = respond.data.items;
      _this.count-- ;
      _this.LoadingClose();
      });
// show Celluar table data
      axios.post("api/property/cellgrowth",{
        page:_this.currentPageCell,
        pageSize:_this.pageSizeCell
      }).then(respond =>{
        _this.cellGrowth = respond.data.items;
        _this.cellTotal = respond.data.total;

        _this.count-- ;
        _this.LoadingClose();
      })
// show disease table data
      axios.post("api/property/diseaseRelated",{
        page:_this.currentPageDisease,
        pageSize:_this.pageSizeCell
      }).then(respond =>{
      _this.disease = respond.data.items;
      _this.diseaseTotal = respond.data.total;
      _this.count-- ;
      _this.LoadingClose();
      })

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
      sessionStorage.setItem('dataBrowse', JSON.stringify(data));
      this.$router.push({
        name:'Gene',
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
      this.currentPageDisease = newPage;
      this.fetchDiseaseData();
    },
    handleHumanChange(newPage) {
      this.currentPageHuman = newPage;
      axios.post("api/property/selectHuman",{
        page:newPage,
        pageSize:20
      }).then(respond =>{
        this.ren = respond.data.items;
        this.humanTotal = respond.data.total;
      });
    },
  }
}
</script>

<style scoped>
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
  width: 90%;
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
