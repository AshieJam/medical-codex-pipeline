import pandas as pd
loinc = pd.read_csv("C:/Users/ashle/Downloads/Files_codexes/Loinc.csv")

##Columns in Loinc dataset
print(loinc.info())

##Checking for appropriate columns for Medical Codexes
### code
print(loinc.LOINC_NUM)

### description
loinc.LONG_COMMON_NAME

###Combination of the two for final output
loinc_draft = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_draft

##Add last updated date
loinc_draft['last_updated'] = '2025-09-12'
loinc_draft

##Rename columns to assignemnent specifications
###loinc_final = loinc_draft.rename(columns={})
loinc_final = loinc_draft.rename(columns={
    'LOINC_NUM': 'code',
    'LONG_COMMON_NAME': 'description'
})
loinc_final

##Export to CSV
file_output_path = "C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/loinc_final.csv"
loinc_final.to_csv ('C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/loinc_final.csv', index=False)