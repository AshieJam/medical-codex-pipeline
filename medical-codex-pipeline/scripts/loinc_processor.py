import pandas as pd
loinc = pd.read_csv("C:/Users/ashle/Downloads/Files_codexes/Loinc.csv")

##Columns in Loinc dataset
print(loinc.info())

##Checking for appropriate columns for Medical Codexes
### code
print(loinc.LOINC_NUM)

### description
loinc.LONG_COMMON_NAME

###last_updated



