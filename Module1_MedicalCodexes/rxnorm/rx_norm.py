import polars as pl
from pathlib import Path

# https://www.nlm.nih.gov/research/umls/rxnorm/docs/techdoc.html#s12_10

file_path = Path('C:/Users/ashle/Downloads/Files_codexes/RXNATOMARCHIVE.RRF')

columns = [
    'rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui'
]

df = pl.read_csv(
    file_path,
    separator='|',
    has_header=False,
    new_columns=columns,
    truncate_ragged_lines=True
)

output_dir = Path('medical-codex-pipeline\output')
output_dir.mkdir(exist_ok=True)
output_path = output_dir / 'RXNATOMARCHIVE.csv'

df.write_csv(output_path)

print(f"Successfully parsed {len(df)} records from RXNATOMARCHIVE.RRF")
print(f"Saved to {output_path}")
print(f"Dataset shape: {df.shape}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nMemory usage (MB): {df.estimated_size() / 1024**2:.2f}")

##Identify the columns best suited for the csv file
df.columns
df.select(['code', 'is_brand'])
df.select(['code', 'str'])

##Combine the columns and last updated
rxnorm_draft = df.select(['code','str'])
rxnorm_draft = rxnorm_draft.with_columns(
    pl.lit('2025-09-12').alias('last_updated')
)

##Rename the columns to assignment specifications
rxnorm_final = rxnorm_draft.rename({
    'code' : 'code',
    'str' : 'description'
})

##Export to CSV
file_output_path = "C:/Users/ashle/HHA-507-2025/medical-codex-pipeline/output/rxnorm_final.csv"
rxnorm_final.write_csv(file_output_path)