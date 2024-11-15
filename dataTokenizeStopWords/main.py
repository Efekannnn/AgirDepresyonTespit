import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

nltk.download('punkt')

stopwords_file = 'turkce-stop-words.txt'
with open(stopwords_file, 'r', encoding='utf-8') as f:
    turkish_stop_words = set(line.strip() for line in f if line.strip())


def preprocess_text(text):
    tokens = word_tokenize(str(text).lower())
    cleaned_tokens = [
        word for word in tokens if word.isalpha() and word not in turkish_stop_words
    ]
    return ' '.join(cleaned_tokens)


file_path = 'data/translated_Anxiety_reddit_posts.csv'
data = pd.read_csv(file_path, usecols=[1])
data.columns = ['text']

data['cleaned_text'] = data['text'].apply(preprocess_text)

output_file = 'cleaned_Anxiety_posts.csv'
data[['cleaned_text']].to_csv(output_file, index=False)

print("Cleaned data saved to:", output_file)
