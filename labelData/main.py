import pandas as pd

cleaned_data_file = 'data/cleaned_turkaa_posts.csv'
data = pd.read_csv(cleaned_data_file)

data['label'] = 0

labeled_output_file = 'labeled_cleaned_turkaa_posts.csv'
data.to_csv(labeled_output_file, index=False)

print("Labeled data saved to:", labeled_output_file)