"""Translate English Reddit posts to Turkish and apply basic cleaning.

Reads raw posts from ``data/raw/`` and writes translated posts to
``data/translated/``.
"""
import re
from pathlib import Path

import nltk
import pandas as pd
from deep_translator import GoogleTranslator

nltk.download("punkt")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "SuicideData.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "translated" / "translated_Suicide_reddit_posts.csv"

translator = GoogleTranslator(source="en", target="tr")


def split_text(text: str, max_length: int = 5000) -> list[str]:
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


def translate_and_clean(text: str) -> str:
    if pd.isna(text):
        return ""

    text = re.sub(r"[^a-zA-Z]+", " ", text).strip().lower()

    translated_text = ""
    for part in split_text(text):
        try:
            translated_text += translator.translate(part) + " "
        except Exception as exc:  # noqa: BLE001 - keep going on translation errors
            print(f"Error translating part: {exc}")
            translated_text += part

    return translated_text.strip()


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(INPUT_FILE)
    data.columns = ["text"]
    data["translated_text"] = data["text"].apply(translate_and_clean)
    data.to_csv(OUTPUT_FILE, index=False)
    print(f"Translated data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
