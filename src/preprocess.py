"""Tokenize translated posts and remove Turkish stop words.

Reads translated posts from ``data/translated/`` and writes the cleaned
text to ``data/cleaned/``.
"""
from pathlib import Path

import nltk
import pandas as pd
from nltk.tokenize import word_tokenize

nltk.download("punkt")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STOPWORDS_FILE = PROJECT_ROOT / "resources" / "turkish_stopwords.txt"
INPUT_FILE = PROJECT_ROOT / "data" / "translated" / "translated_Anxiety_reddit_posts.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "cleaned" / "cleaned_Anxiety_posts.csv"

with open(STOPWORDS_FILE, "r", encoding="utf-8") as f:
    TURKISH_STOP_WORDS = {line.strip() for line in f if line.strip()}


def preprocess_text(text: str) -> str:
    tokens = word_tokenize(str(text).lower())
    cleaned_tokens = [
        word for word in tokens if word.isalpha() and word not in TURKISH_STOP_WORDS
    ]
    return " ".join(cleaned_tokens)


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(INPUT_FILE, usecols=[1])
    data.columns = ["text"]
    data["cleaned_text"] = data["text"].apply(preprocess_text)
    data[["cleaned_text"]].to_csv(OUTPUT_FILE, index=False)
    print(f"Cleaned data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
