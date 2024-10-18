# 更新数据库的fa文件
# 创建数据连接
import pandas as pd
from sqlalchemy import create_engine, text

# 数据库连接信息
username = 'root'
password = 'auggie'
host = '192.168.123.166'  # 通常是 'localhost'
port = 3306  # 默认 MySQL 端口号
database = 'dbess'


# 使用SQLAlchemy创建数据库引擎
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

# # 解析trans.fa文件
# def parse_fa_file(fa_file):
#     sequences = {}
#     with open(fa_file, 'r', encoding='utf-8') as file:
#         transcript_id = ""
#         seq = ""
#         for line in file:
#             if line.startswith(">"):
#                 if transcript_id and seq:
#                     sequences[transcript_id] = seq
#                 transcript_id = line.strip()[1:]  # 去掉 '>'
#                 seq = ""
#             else:
#                 seq += line.strip()
#         if transcript_id and seq:
#             sequences[transcript_id] = seq  # 添加最后一个序列
#     return sequences

# def update_database(fa_file, engine):
#     # 解析fa文件
#     sequences = parse_fa_file(fa_file)
    
#     with engine.connect() as connection:
    
#         for Lncbook_trans_id, sequence in sequences.items():
#             update_query = text("""
#                 UPDATE trans
#                 SET FASTA = CONCAT('>', transcript_id, '|', Lncbook_trans_id, '<br/>', :sequence)
#                 WHERE Lncbook_trans_id = :Lncbook_trans_id
#             """)
#             connection.execute(update_query, {"sequence": sequence, "Lncbook_trans_id": Lncbook_trans_id})
#         connection.commit()



# 路径
fa_file = './map/LncBookv2_OnlyLnc.fa'
txt_file = './map/lnc_trans.txt'
df = pd.read_csv(txt_file, sep='\t', header=0)
trans = set(df['Lncbook_trans_id'])
# print(trans)
with engine.connect() as connection:
    with open(fa_file, 'r', encoding='utf-8') as file:
        Lncbook_trans_id = ""
        seq = ""
        for line in file:
            if line.startswith(">"):
                if Lncbook_trans_id and seq and Lncbook_trans_id in trans:
                    update_query = text("""
                        UPDATE trans
                        SET FASTA = CONCAT('>', transcript_id, '|', Lncbook_trans_id, '<br/>', :sequence)
                        WHERE Lncbook_trans_id = :Lncbook_trans_id
                    """)
                    connection.execute(update_query, {"sequence": seq, "Lncbook_trans_id": Lncbook_trans_id})
                Lncbook_trans_id = line.strip()[1:]
                seq = ""
            else:
                seq += line.strip()
        if Lncbook_trans_id and seq and Lncbook_trans_id in trans:
                update_query = text("""
                        UPDATE trans
                        SET FASTA = CONCAT('>', transcript_id, '|', Lncbook_trans_id, '<br/>', :sequence)
                        WHERE Lncbook_trans_id = :Lncbook_trans_id
                    """)
                connection.execute(update_query, {"sequence": seq, "Lncbook_trans_id": Lncbook_trans_id})
    connection.commit()
    print("数据已成功更新到MySQL数据库中。")

