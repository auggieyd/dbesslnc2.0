import pandas as pd

# 1. Read the input files
transcript_file = pd.read_csv('../exon/lnc_trans_exon.csv', sep=',')  # LncBook transcript file
exp_file = pd.read_csv('expression_profiles_HPA/HPATranscriptTPM_MEAN.tsv', sep='\t')  # Read the TSV file

transcript_file = transcript_file[['UID', 'Lncbook_trans_id', 'Organism']]

# 2. Select the columns of interest
cols_exp = ['Lncbook_trans_id', 'brain', 'lung', 'urinarybladder', 'kidney', 'adrenal', 'thyroid', 'heart', 'lymphnode', 'spleen',
            'bonemarrow', 'tonsil', 'appendix', 'colon', 'esophagus', 'gallbladder', 'smallintestine', 'salivarygland',
            'stomach', 'liver', 'duodenum', 'pancreas', 'rectum', 'endometrium', 'ovary', 'testis', 'prostate',
            'fallopiantube', 'skeletalmuscle', 'smoothmuscle', 'skin', 'fat']  # Names of tissues to display expression levels
exp_file = exp_file[cols_exp]

# 3. Retain transcripts with Lncbook_trans_id
lncbook_transcripts = transcript_file[transcript_file['Lncbook_trans_id'] != "N.A."]

# 4. Match expression profiles based on transcript IDs
trans_exp = pd.merge(lncbook_transcripts, exp_file, on='Lncbook_trans_id', how='inner')
trans_exp.loc[:, 'transcript_id'] = trans_exp['Lncbook_trans_id']

# 5. Save the result to a CSV file
trans_exp.to_csv('exp_profile.csv', index=False)

print("Processing complete. Results have been saved to lit_exp_profile.csv.")
