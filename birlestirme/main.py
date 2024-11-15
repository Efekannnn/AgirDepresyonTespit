import pandas as pd
import os

csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]

dataframes = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(dataframes, ignore_index=True)

combined_df = combined_df.dropna(how='any')
combined_df = combined_df.drop_duplicates()

output_file = 'combined_cleaned_data.csv'
combined_df.to_csv(output_file, index=False)

print(f"Birleştirilmiş ve temizlenmiş veri kaydedildi: {output_file}")