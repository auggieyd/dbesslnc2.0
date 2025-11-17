# dbEssLnc2.0: exploring disease-associated essential long non-coding RNAs in human cell lines
**dbEssLnc2.0** is a major update to the previously published dbEssLnc database. We are dedicated to building a comprehensive, high-quality repository of essential long non-coding RNA (lncRNA) genes in humans, particularly focusing on their roles in cancer and genetic diseases. dbEssLnc2.0 can be accessible freely at https://esslnc.pufengdu.org/v2/.

## 🎯 Core Updates and Value Proposition

Compared to the previous version, dbEssLnc2.0 features the following key enhancements:

1. **Data Volume Increase (Approx. 20-fold)**: Added **2716** new essential lncRNA records, increasing the total collection size by approximately **20 times**.
2. **Experimental Validation Data**: Includes **1,190** experimentally validated essential lncRNAs derived from CRISPR-based genomic screens.
3. **Disease Association**: Added **1,319** putative essential lncRNAs associated with pathogenic variants, significantly enhancing the database's value for computational biology and bioinformatics studies.
4. **New Information**: Integrated novel essentiality classifications, gene annotations, and detailed variant data.

## 📝 Data Collection and Processing Process

For a detailed understanding of how the data in dbEssLnc2.0 was collected, curated, and processed from primary sources, please refer to the dedicated documentation:

- **Data Curated Process:** [Data Curated Process](data_curated/readme.md)

This document provides necessary background and methodology for the bioinformatics and manual curation steps performed to ensure data quality and integrity.


## 🛠️ Deployment Guide: One-Click Launch
To simplify deployment and mirroring tasks, we highly recommend using Docker Compose for a one-click deployment solution. This method configures the Node.js backend, MySQL database, and the necessary BLAST tools simultaneously.

### 1. Prerequisites

- Install **Docker** and **Docker Compose**.
- Place the `dbesslnc2.sql` file in the project's root directory or a path accessible by the Dockerfile.
- Download the [dbesslnc-deployment package](https://github.com/auggieyd/dbesslnc2.0/releases/tag/v1.0.0)

### 2. Deployment Steps

Execute the following commands in the `dbesslnc-deployment` root directory to launch the entire system:

```yaml
# 1. Build images and start all services (Backend, MySQL, BLAST configuration)
cd dbesslnc-deployment
docker-compose up --build -d

# 2. Check container status
docker-compose ps

# 3. Access the website
# Enter http://localhost:8081 or your configured server IP/domain in the browser
```



## ⚙️ Manual Deployment Guide (Legacy/Advanced)

### 1. Server Environment

1. **Install Node.js and npm:** Ensure Node.js (v14+,https://nodejs.org/en/download/) and npm are installed. *(Example for Ubuntu20 systems):.

2. **Install MySQL server**: Ensure MySQL(V8.0,https://www.mysql.com/downloads/) is running.

3. **Install and Configure BLAST+ Tools:** BLAST+ is essential for the database's search functionality. We use version 2.12.0.

   ```shell
   # Download and extract BLAST+ (change directory as needed)
   cd /blast/
   wget https://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.12.0/ncbi-blast-2.12.0+-x64-linux.tar.gz
   tar -zxvf ncbi-blast-2.12.0+-x64-linux.tar.gz
   mv ncbi-blast-2.12.0+ blast+
   rm ncbi-blast-2.12.0+-x64-linux.tar.gz
   
   # Add BLAST binaries to the system PATH (modify based on your shell profile)
   echo 'export PATH="/usr/local/blast+/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   
   # Verify installation
   blastn -version
   
   # Build the lncRNA Database Index 
   # NOTE: This assumes lncRNA2.fasta is located in the project's 'blast/lncrna/' directory.
   cd /path/to/your/project/root
   makeblastdb -in blast/lncrna/lncRNA2.fasta -dbtype nucl
   
   ```

   

### 1. Frontend (Vue + Element Plus)

1.  Install dependencies:

   ```
   cd dbEssLnc2.0
   npm install
   ```

2. Execute production build:

   ```
   npm run build
   cd dist
   mv -f md assets data v2/ 
   ```

### 2. Backend (Node.js + Express)

1. Navigate to the backend directory and install dependencies:

   ```
   cd server
   npm install
   ```

2. Start the backend service using PM2 or another process manager:

   ```
   # Recommended to use PM2 for process management
   npm install -g pm2
   pm2 start index.js --name dbEssLnc2.0-backend
   ```

### 3. Database (MySQL)

1. Create the database:

   ```
   mysql -u [user] -p 
   CREATE DATABASE dbess2;
   ```

2. Import the SQL file:

   ```
   source /path-to/dbesslnc2.sql;
   ```
3. Modify the backend configuration file to connect to the correct MySQL instance.

### 4. Access the Website

After successfully starting the backend service (Step 2) and configuring the web server (Nginx/Apache) to serve the frontend build (Step 1), open your web browser.

```
# Access the website using your server's configured domain name or IP address:
# Example: http://localhost:8081 or http://your_domain_name
```



## Citation
Zhang YY, Zhang WY, Xin XH, Du PF. dbEssLnc: A manually curated database of human and mouse essential lncRNA genes. Comput Struct Biotechnol J. 2022 May 23;20:2657-2663. doi: 10.1016/j.csbj.2022.05.043. PMID: 35685362; PMCID: PMC9162909.
