var express = require("express");
var router = express.Router();
var mysql = require("mysql2");
var $sql = require("../sqlMap");
var exec = require('child_process').exec;
let randomStr = require('string-random'); 
var fs = require("fs");
var path = require("path");



// Paths for BLAST databases
const BLASTDB = ""
// Server path for BLAST queries and results
// const tempPath_query = "/home/path/blast/temp/"
// const tempPath_result= "/home/path/dbesslnc/blast/temp/" 
// const db_path = "/home/path/dbesslnc/blast/lncrna/lncrna.fasta"
// Local path for BLAST queries and results
const tempPath_query = path.join(__dirname, '../../blast/temp/');
const tempPath_result = path.join(__dirname, '../../blast/temp/');
const db_path = path.join(__dirname, '../../blast/lncrna/lncRNA2.fasta');


const {MYSQL_CONFIG} = require('../db.js');
// var blast = require("../blast.js")
// Create connection
var connection = mysql.createConnection(MYSQL_CONFIG);
// Connect to database
connection.connect();
// Build hierarchical data


// Convert data to JSON format
var jsonWrite = function(res, ret) {
  if (typeof ret === "undefined") {
    res.json({
      code: "1",
      msg: "error"
    });
  } else {
    res.json(ret);
  }
};

let options ={
  flags: "a",
  encoding:'utf8'
}
let stderr = fs.createWriteStream('./a.log',options);
let logger = new console.Console(stderr);
fs.writeFile('./a.log','',function(err){
  if(err){
    console.log(err)
  }
});
// SQL statements for the browser page
//show final table
router.post("/final", (req, res) => {
  var sql = $sql.property.selectFinal;
  connection.query(sql, function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, result);
    }
  });
});
//show vital table
router.post("/vital", (req, res) => {
  var sql = $sql.property.selectVital;
  connection.query(sql, function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, result);
    }
  });
});
//show tumor table
router.post("/tumor", (req, res) => {
  var sql = $sql.property.selectTumor;
  connection.query(sql, function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, result);
    }
  });
});
//show cancer table
router.post("/cancer", (req, res) => {
  var sql = $sql.property.selectCancer;
  connection.query(sql, function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, result);
    }
  });
});
// show cell growth table
router.post("/cellGrowth", (req, res) => {
  const {page,pageSize} = req.body;
  const offset = (page-1)*pageSize;
  var sql = $sql.property.select_cell_growth;
  var count = $sql.property.cell_count;
  connection.query(sql,[offset, pageSize], function(err, result) {
    if (result) {

      connection.query(count, function(err, countResult) {
          if (err) {
            return res.status(500).send(err.message);
          }
          const total = countResult[0].total;
          jsonWrite(res, { items: result, total: total });
        });
    }
  });
});
// show diease related table
router.post("/diseaseRelated", (req, res) => {
  const {page,pageSize} = req.body;
  // log request body
  const offset = (page-1)*pageSize;
  var sql = $sql.property.select_diease_related;
  var count = $sql.property.disease_count;
  connection.query(sql,[offset,pageSize] , function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      connection.query(count, function(err, countResult) {
        if (err) {
          return res.status(500).send(err.message);
        }
        const total = countResult[0].total;
        jsonWrite(res, { items: result, total: total });
      });
    }
  });
});
router.post("/diseaseMap", (req, res) => {
  var sql = $sql.property.selectDiseaseMap;
  var UID = req.body.UID;
  connection.query(sql,[UID], function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result && result.length > 0) {
      const variationIds = result.map(row => row.variation_id);
      connection.query($sql.property.selectDisease, [variationIds], function(err, diseaseResult) {
        if (err) {  
          return res.status(500).send(err.message);
        }
        if (diseaseResult) {
          const response = {
            UID: UID,
            disease: diseaseResult
          }
          jsonWrite(res, response);
        }
      });
    }
  });
});

//search page
//organism is human
router.post("/selectHuman", (req, res) => {
  var sql = $sql.property.selectHuman;
  const {page,pageSize} = req.body;
  // log request body
  const offset = (page-1)*pageSize;
  connection.query(sql, [offset, pageSize], function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, {items: result, total: 6281});
    }
  });
});
//organism is mouse
router.post("/selectMouse", (req, res) => {
  var sql = $sql.property.selectMouse;
  const {page,pageSize} = req.body;
  const offset = (page-1)*pageSize;
  connection.query(sql, [offset,pageSize], function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, {items: result, total: 34});
    }
  });
});
//reason is vital
router.post("/select_reason_vital", (req, res) => {
  var sql = $sql.property.select_reason_vital;
  const {page,pageSize} = req.body;

  const offset = (page-1)*pageSize;
  connection.query(sql, [offset,pageSize], function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, {items: result, total: 40});
    }
  });
});
//reason is tumor
router.post("/select_reason_tumor", (req, res) => {
  var sql = $sql.property.select_reason_tumor;
  const {page,pageSize} = req.body;
  // log request body
  const offset = (page-1)*pageSize;
  connection.query(sql,[offset, pageSize], function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {
      jsonWrite(res, {items: result, total: 117});
    }
  });
});
//reason is cancer
router.post("/select_reason_cancer", (req, res) => {
  var sql = $sql.property.select_reason_cancer;
  const {page,pageSize} = req.body;
  const offset = (page-1)*pageSize;
  connection.query(sql,[offset, pageSize], function(err, result) {
    if (err) {
      return res.status(500).send(err.msg);
    }
    if (result) {

      jsonWrite(res, {items: result, total: 88});
    }
  });
});


//quzzy search 

router.post("/searchHuman",(req,res)=> {
  var sql=$sql.property.searchHuman;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/searchMouse",(req,res)=> {
  var sql=$sql.property.searchMouse;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/searchVital",(req,res)=> {
  var sql=$sql.property.searchVital;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/searchTumor",(req,res)=> {
  var sql=$sql.property.searchTumor;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/searchCancer",(req,res)=> {
  var sql=$sql.property.searchCancer;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/searchDisease",(req,res)=> {
  var sql=$sql.property.searchDisease;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});
router.post("/searchCell",(req,res)=> {
  var sql=$sql.property.searchCell;
  var proName = req.body;
  connection.query(sql,[proName.inputContent],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

//fuzzy search
router.post("/fuzzyHuman",(req,res)=> {
  var sql=$sql.property.fuzzyHuman;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/fuzzyMouse",(req,res)=> {
  var sql=$sql.property.fuzzyMouse;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/fuzzyVital",(req,res)=> {
  var sql=$sql.property.fuzzyVital;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/fuzzyTumor",(req,res)=> {
  var sql=$sql.property.fuzzyTumor;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/fuzzyCancer",(req,res)=> {
  var sql=$sql.property.fuzzyCancer;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/fuzzyDisease",(req,res)=> {
  var sql=$sql.property.fuzzyDisease;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});

router.post("/fuzzyCell",(req,res)=> {
  var sql=$sql.property.fuzzyCell;
  connection.query(sql,(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
});


router.post("/blast",(req,res)=>{

  if(
      typeof req.body.user_seq == "undefined"
      ||typeof req.body.user_eValue == "undefined"
      ||typeof req.body.user_wordSize == "undefined"
      ){
        res.status(400);
        res.send({
          error:true,
          message:"post parameter missing(user_seq,user_eValue)"
        })
      }
      else{
        let inputFile = randomStr();
        let outputFile = randomStr();
        var user_seq = req.body.user_seq;
        var user_wordSize = req.body.user_wordSize.toString();
        var user_eValue = req.body.user_eValue.toString();
        var path_query = tempPath_query + inputFile + '.fasta';
        var path_result = tempPath_result + outputFile + '.txt';

        fs.writeFileSync(path_query, user_seq); 
        fs.writeFileSync(path_result,"");   


        var cmd = BLASTDB+'blastn -query '+path_query+
                  ' -out '+path_result+
                  ' -db '+db_path+
                  ' -outfmt "6 qseqid sseqid pident length evalue bitscore "'+
                  ' -evalue '+user_eValue+
                  ' -word_size '+user_wordSize;

        logger.log(cmd);
        exec(cmd, function(error, stdout, stderr) {

          let data = fs.readFileSync(path_result, "utf8").split('\n'); 
          logger.log(data)

            res.send({
              error: false,
              message: {
                  num: 0,
                  info: error,stdout,stderr,
                  data:data
              },
          });
          fs.close;
          fs.unlinkSync(path_query);
          fs.unlinkSync(path_result);
          return;
      });

        
      }
})


router.post("/fuzzySeq",(req,res)=> {
  //var sql=$sql.property.fuzzySeq;  
  var alignId = req.body.alignId;
  var sql = "select * from `trans` where transcript_id = ?";
  connection.query(sql,[alignId],(err,result)=>{
    
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){      
      jsonWrite(res,result);
      
    }
   
  })
})

router.post("/profiles",(req,res)=> {

  var RNAid=req.body.RNAid;
  var UID = req.body.UID;
  var Organism = req.body.Organism;

  if(Organism === "Human"){
    var sql=$sql.property.profileHuman;
  }else var sql=$sql.property.profileMouse;
  connection.query(sql,[RNAid, UID],(err,result)=>{
 
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){

      jsonWrite(res,result);
      
    }
    
  })
})
router.post("/transcript",(req,res)=> {

  // var DNAid=req.body.DNAid;
  var DNAid = req.body.UID;
  
  var sql=$sql.property.transcript;
  connection.query(sql,[DNAid],(err,result)=>{
    
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
      
    }
    
  })
})
router.post("/gene",(req,res)=> {
  var sql=$sql.property.gene;
  var UID = req.body.UID;
  connection.query(sql,[UID],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
})

router.post("/experiment",(req,res)=> {
  var sql=$sql.property.experiment;
  var UID = req.body.UID;
  connection.query(sql,[UID],(err,result)=>{
    if(err) {
      return res.status(500).send(err.msg);
    }
    if(result){
      jsonWrite(res,result);
    }
  })
})


module.exports = router;
