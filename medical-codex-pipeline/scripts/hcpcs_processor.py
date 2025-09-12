import pandas as pd
hcpcs_file = pd.read_csv("C:/Users/ashle/Downloads/Files_codexes/HCPC2025_OCT_ANWEB_v3.csv")
hcpcs_file

##Checking the appropriate columms
print(hcpcs_file.info())

##Code
print(hcpcs_file.HCPC)

##Description
print(hcpcs_file["LONG DESCRIPTION"])

## Combination
hcpcs_draft = hcpcs_file[['HCPC','LONG DESCRIPTION']]
hcpcs_draft

##Add Last Updated Date
hcpcs_draft['last_updated'] = '2025-09-12'

hcpcs_draft

### Rename colums to assigntment specfications
hcpcs_final = hcpcs_draft.rename(columns={
    'HCPC': 'code',
    'LONG DESCRIPTION': 'description'
})

##Export to CSV
file_output_path = "C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/hcpcs_final.csv"
hcpcs_final.to_csv ('C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/hcpcs_final.csv', index = False)

