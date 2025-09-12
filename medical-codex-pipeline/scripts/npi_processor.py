##Testing out polars
import polars as pl
import pandas as pd

npi_file_path = "C:/Users/ashle/Downloads/Files_codexes/npidata_pfile_20050523-20250907.csv"

npi_csv = pl.read_csv("C:/Users/ashle/Downloads/Files_codexes/npidata_pfile_20050523-20250907.csv", n_rows=60)

print(npi_csv)

print(npi_csv.columns)

##Code column
print(npi_csv["NPI"])

##Description column
print(npi_csv['Provider Last Name (Legal Name)'])

##Combine the columns
npi_draft = npi_csv.select([
    'NPI',
    'Provider Last Name (Legal Name)'])

print(npi_draft)

##Add last updated date
npi_draft = npi_draft.with_columns(
    pl.lit('2025-09-12').alias('last_updated')
)

npi_draft

##Rename the columns to assignment specifications
npi_final = npi_draft.rename({
    'NPI' : 'code',
    'Provider Last Name (Legal Name)' : 'description'
})

npi_final

##Export to CSV
file_output_path = "C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/npi_final.csv"
npi_final.write_csv(file_output_path)
