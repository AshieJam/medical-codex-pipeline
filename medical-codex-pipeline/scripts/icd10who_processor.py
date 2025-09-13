import pandas as pd

file_path = 'C:/Users/ashle/Downloads/Files_codexes/icd102019syst_codes.txt'

columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3', 'morbidity_code4']

df = pd.read_csv(file_path, sep=';', header=None, names=columns)

output_path = 'medical-codex-pipeline/output/icd10who.csv'
df.to_csv(output_path, index=False)

print(f"Successfully parsed {len(df)} records from {file_path}")
print(f"Saved to {output_path}")
print(f"/nFirst 5 rows:")
print(df.head())

icd_who = pd.read_csv("medical-codex-pipeline/output/icd10who.csv")
icd_who

##Searching columns
icd_who.columns
icd_who.icd10_code
icd_who.detailed_title

##Combination of code and description
icd_who_draft = icd_who[['icd10_code','detailed_title']]
icd_who_draft

##Add Last Updated Date
icd_who_draft['last_updated'] = '2025-09-12'

##Rename colums to assigntment specfications
icd_who_final = icd_who_draft.rename(columns={
    'icd10_code': 'code',
    'detailed_title': 'description'
})  

##Export to CSV
file_output_path = "C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/icd10who_final.csv"
icd_who_final.to_csv (file_output_path, index = False)
icd_who_final
