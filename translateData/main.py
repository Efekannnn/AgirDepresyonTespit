from deep_translator import GoogleTranslator
import pandas as pd
import nltk
import re

nltk.download('punkt')
file_path = 'SuicideData.csv'
data = pd.read_csv(file_path)
data.columns = ['text']

translator = GoogleTranslator(source='en', target='tr')


def split_text(text, max_length=5000):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


def translate_and_clean(text):
    if pd.isna(text):
        return ""

    text = re.sub(r'[^a-zA-Z]+', ' ', text).strip().lower()
    text = text.lower()

    text_parts = split_text(text)

    translated_text = ""
    for part in text_parts:
        try:
            translated_text += translator.translate(part) + " "
        except Exception as e:
            print(f"Error translating part: {e}")
            translated_text += part

    return translated_text.strip()


data['translated_text'] = data['text'].apply(translate_and_clean)

data.to_csv('translated_Suicide_reddit_posts.csv', index=False)