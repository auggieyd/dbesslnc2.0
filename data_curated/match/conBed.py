#!/usr/bin/env python3
# filepath: gtf_to_bed_fixed.py

import re
import sys
import argparse

def extract_attribute(attributes, key):
    """从GTF属性字符串中提取指定属性值"""
    pattern = f'{key} "([^"]*)"'
    match = re.search(pattern, attributes)
    return match.group(1) if match else ""

def extract_gene_id_from_db_xref(attributes):
    """从db_xref中提取GeneID"""
    pattern = r'db_xref "GeneID:(\d+)"'
    match = re.search(pattern, attributes)
    return match.group(1) if match else ""

def normalize_chromosome(seqname):
    """
    标准化染色体名称,确保有chr前缀
    """
    # 如果已经有chr前缀，直接返回
    if seqname.startswith('chr'):
        return seqname
    
    # 处理常见的染色体命名格式
    # NC_000001.11 -> chr1
    if seqname.startswith('NC_'):
        # 提取染色体编号
        match = re.match(r'NC_0+(\d+)\.', seqname)
        if match:
            chr_num = match.group(1)
            if chr_num == '23':
                return 'chrX'
            elif chr_num == '24':
                return 'chrY'
            else:
                return f'chr{chr_num}'
    
    # 如果是数字，添加chr前缀
    if seqname.isdigit():
        return f'chr{seqname}'
    
    # 如果是X, Y, M等，添加chr前缀
    if seqname in ['X', 'Y', 'M', 'MT']:
        return f'chr{seqname}'
    
    # 其他情况，直接添加chr前缀
    if not seqname.startswith('chr'):
        return f'chr{seqname}'
    
    return seqname

def gtf_to_bed(gtf_file, output_bed, feature_types=['gene'], add_chr_prefix=True):
    """
    将GTF文件转换为BED格式
    
    参数:
    gtf_file: 输入GTF文件路径
    output_bed: 输出BED文件路径  
    feature_types: 要包含的特征类型列表
    add_chr_prefix: 是否添加chr前缀
    """
    
    bed_records = []
    
    print(f"正在处理GTF文件: {gtf_file}")
    print(f"提取特征类型: {', '.join(feature_types)}")
    print(f"添加chr前缀: {add_chr_prefix}")
    
    with open(gtf_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            # 跳过注释行
            if line.startswith('#'):
                continue
                
            line = line.strip()
            if not line:
                continue
                
            fields = line.split('\t')
            if len(fields) < 9:
                continue
            
            # 解析GTF字段
            seqname = fields[0]
            source = fields[1] 
            feature = fields[2]
            start = int(fields[3]) - 1  # GTF是1-based，BED是0-based
            end = int(fields[4])
            score = fields[5] if fields[5] != '.' else '0'
            strand = fields[6]
            frame = fields[7]
            attributes = fields[8]
            
            # 只处理指定的特征类型
            if feature not in feature_types:
                continue
            
            # 标准化染色体名称
            if add_chr_prefix:
                chromosome = normalize_chromosome(seqname)
            else:
                chromosome = seqname
            
            # 提取关键属性
            gene_id = extract_attribute(attributes, 'gene_id')
            transcript_id = extract_attribute(attributes, 'transcript_id')
            gene_name = extract_attribute(attributes, 'gene')
            gene_biotype = extract_attribute(attributes, 'gene_biotype')
            transcript_biotype = extract_attribute(attributes, 'transcript_biotype')
            geneid = extract_gene_id_from_db_xref(attributes)
            
            # 构建BED记录名称
            if feature == 'gene':
                name = f"{gene_name}|{gene_id}|{gene_biotype}" if gene_biotype else f"{gene_name}|{gene_id}"
            elif feature == 'transcript':
                biotype = transcript_biotype if transcript_biotype else gene_biotype
                name = f"{gene_name}|{transcript_id}|{biotype}" if biotype else f"{gene_name}|{transcript_id}"
            elif feature == 'exon':
                exon_number = extract_attribute(attributes, 'exon_number')
                biotype = transcript_biotype if transcript_biotype else gene_biotype
                name = f"{gene_name}|{transcript_id}|exon{exon_number}|{biotype}" if biotype else f"{gene_name}|{transcript_id}|exon{exon_number}"
            else:
                name = f"{gene_name}|{gene_id}|{feature}"
            
            # 创建BED记录
            bed_record = {
                'chr': chromosome,
                'start': start,
                'end': end,
                'name': name,
                'score': score,
                'strand': strand,
                'gene_id': gene_id,
                'transcript_id': transcript_id,
                'feature': feature,
                'gene_name': gene_name,
                'gene_biotype': gene_biotype,
                'geneid': geneid  # 新增的GeneID列
            }
            
            bed_records.append(bed_record)
            
            if line_num % 10000 == 0:
                print(f"已处理 {line_num} 行...")
    
    # 按染色体和位置排序
    print("正在排序记录...")
    def chr_sort_key(record):
        chr_name = record['chr']
        # 提取数字部分用于排序
        if chr_name.startswith('chr'):
            chr_part = chr_name[3:]
            if chr_part.isdigit():
                return (0, int(chr_part), record['start'])
            elif chr_part == 'X':
                return (1, 0, record['start'])
            elif chr_part == 'Y':
                return (1, 1, record['start'])
            elif chr_part in ['M', 'MT']:
                return (1, 2, record['start'])
            else:
                return (2, chr_part, record['start'])
        else:
            return (3, chr_name, record['start'])
    
    bed_records.sort(key=chr_sort_key)
    
    # 写入BED文件
    print(f"正在写入BED文件: {output_bed}")
    with open(output_bed, 'w') as f:
        # 写入标题行
        f.write("#chr\tstart\tend\tname\tscore\tstrand\tgene_id\ttranscript_id\tfeature\tgene_name\tgene_biotype\tGeneID\n")
        
        for record in bed_records:
            line = f"{record['chr']}\t{record['start']}\t{record['end']}\t{record['name']}\t{record['score']}\t{record['strand']}\t{record['gene_id']}\t{record['transcript_id']}\t{record['feature']}\t{record['gene_name']}\t{record['gene_biotype']}\t{record['geneid']}\n"
            f.write(line)
    
    print(f"转换完成！")
    print(f"总共处理了 {len(bed_records)} 条记录")
    
    # 显示染色体统计
    chr_counts = {}
    for record in bed_records:
        chr_name = record['chr']
        chr_counts[chr_name] = chr_counts.get(chr_name, 0) + 1
    
    print("\n染色体统计:")
    for chr_name in sorted(chr_counts.keys(), key=lambda x: chr_sort_key({'chr': x, 'start': 0})):
        print(f"  {chr_name}: {chr_counts[chr_name]}")

def filter_lncrna_and_convert(gtf_file, output_bed, add_chr_prefix=True):
    """
    专门提取lncRNA相关记录并转换为BED格式
    """
    
    print("正在提取lncRNA基因...")
    
    # 第一步：找到所有lncRNA基因的gene_id
    lncrna_genes = set()
    
    with open(gtf_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
                
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue
                
            feature = fields[2]
            attributes = fields[8]
            
            if feature == 'gene' and 'gene_biotype "lncRNA"' in attributes:
                gene_id = extract_attribute(attributes, 'gene_id')
                if gene_id:
                    lncrna_genes.add(gene_id)
    
    print(f"找到 {len(lncrna_genes)} 个lncRNA基因")
    
    # 第二步：提取相关记录并转换为BED
    bed_records = []
    
    with open(gtf_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
                
            fields = line.strip().split('\t')
            if len(fields) < 9:
                continue
            
            seqname = fields[0]
            feature = fields[2]
            attributes = fields[8]
            gene_id = extract_attribute(attributes, 'gene_id')
            
            # 只处理lncRNA基因的gene、transcript、exon
            if gene_id in lncrna_genes and feature in ['gene', 'transcript', 'exon']:
                start = int(fields[3]) - 1  # GTF转BED坐标
                end = int(fields[4])
                strand = fields[6]
                
                # 标准化染色体名称
                if add_chr_prefix:
                    chromosome = normalize_chromosome(seqname)
                else:
                    chromosome = seqname
                
                transcript_id = extract_attribute(attributes, 'transcript_id')
                gene_name = extract_attribute(attributes, 'gene')
                gene_biotype = extract_attribute(attributes, 'gene_biotype')
                transcript_biotype = extract_attribute(attributes, 'transcript_biotype')
                geneid = extract_gene_id_from_db_xref(attributes)
                
                # 构建名称
                if feature == 'gene':
                    name = f"{gene_name}|{gene_id}|lncRNA"
                elif feature == 'transcript':
                    name = f"{gene_name}|{transcript_id}|lncRNA"
                elif feature == 'exon':
                    exon_number = extract_attribute(attributes, 'exon_number')
                    name = f"{gene_name}|{transcript_id}|exon{exon_number}|lncRNA"
                
                bed_record = {
                    'chr': chromosome,
                    'start': start,
                    'end': end,
                    'name': name,
                    'score': '0',
                    'strand': strand,
                    'gene_id': gene_id,
                    'transcript_id': transcript_id,
                    'feature': feature,
                    'gene_name': gene_name,
                    'gene_biotype': gene_biotype,
                    'geneid': geneid
                }
                
                bed_records.append(bed_record)
    
    # 排序并写入
    def chr_sort_key(record):
        chr_name = record['chr']
        if chr_name.startswith('chr'):
            chr_part = chr_name[3:]
            if chr_part.isdigit():
                return (0, int(chr_part), record['start'])
            elif chr_part == 'X':
                return (1, 0, record['start'])
            elif chr_part == 'Y':
                return (1, 1, record['start'])
            else:
                return (2, chr_part, record['start'])
        else:
            return (3, chr_name, record['start'])
    
    bed_records.sort(key=chr_sort_key)
    
    with open(output_bed, 'w') as f:
        f.write("#chr\tstart\tend\tname\tscore\tstrand\tgene_id\ttranscript_id\tfeature\tgene_name\tgene_biotype\tGeneID\n")
        
        for record in bed_records:
            line = f"{record['chr']}\t{record['start']}\t{record['end']}\t{record['name']}\t{record['score']}\t{record['strand']}\t{record['gene_id']}\t{record['transcript_id']}\t{record['feature']}\t{record['gene_name']}\t{record['gene_biotype']}\t{record['geneid']}\n"
            f.write(line)
    
    print(f"lncRNA BED文件已保存: {output_bed}")
    print(f"包含 {len(bed_records)} 条记录")

def main():
    parser = argparse.ArgumentParser(description='将GTF文件转换为BED格式')
    parser.add_argument('gtf_file', help='输入GTF文件')
    parser.add_argument('output_bed', help='输出BED文件')
    parser.add_argument('--features', nargs='+', default=['gene'], 
                       help='要提取的特征类型 (默认: gene)')
    parser.add_argument('--lncrna-only', action='store_true',
                       help='只提取lncRNA相关记录')
    parser.add_argument('--no-chr-prefix', action='store_true',
                       help='不添加chr前缀，保持原始染色体名称')
    
    args = parser.parse_args()
    
    add_chr_prefix = not args.no_chr_prefix
    
    if args.lncrna_only:
        filter_lncrna_and_convert(args.gtf_file, args.output_bed, add_chr_prefix)
    else:
        gtf_to_bed(args.gtf_file, args.output_bed, args.features, add_chr_prefix)

if __name__ == "__main__":
    main()