import pandas as pd

# 1. Read the input files
transcript_file = pd.read_csv('trans_UID.txt', sep='\t')  # LncBook transcript file
exp_file = pd.read_csv('expression_profiles_HPA/HPATranscriptTPM_MEAN.tsv', sep='\t')  # Read the TSV file

# 2. Select the columns of interest
cols_exp = ['Lncbook_trans_id', 'brain', 'lung', 'urinarybladder', 'kidney', 'adrenal', 'thyroid', 'heart', 'lymphnode', 'spleen',
            'bonemarrow', 'tonsil', 'appendix', 'colon', 'esophagus', 'gallbladder', 'smallintestine', 'salivarygland',
            'stomach', 'liver', 'duodenum', 'pancreas', 'rectum', 'endometrium', 'ovary', 'testis', 'prostate',
            'fallopiantube', 'skeletalmuscle', 'smoothmuscle', 'skin', 'fat']  # Names of tissues to display expression levels
exp_file = exp_file[cols_exp]

# 3. Match expression profiles based on transcript IDs
trans_exp = pd.merge(transcript_file, exp_file, on='Lncbook_trans_id', how='inner')

# 4. Save the result to a CSV file
trans_exp.to_csv('exp_profile.csv', index=False)

print("Processing complete. Results have been saved to exp_profile.csv.")
