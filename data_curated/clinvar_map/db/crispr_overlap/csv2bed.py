import pandas as pd

# 读取CSV文件，正确处理内部逗号
df = pd.read_csv('../conversion/lncRNA_with_etrez_symbol.csv', sep=',', quotechar='"')

# 将DataFrame保存为BED格式，用制表符分隔
df.to_csv('final_lncRNA.bed', sep='\t', index=False, header=False)
