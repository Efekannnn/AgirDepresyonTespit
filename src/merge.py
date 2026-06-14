"""Merge all labeled CSV files into a single cleaned, deduplicated dataset.

Reads every CSV in ``data/labeled/`` and writes the combined dataset to
``data/combined/``.
"""
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "data" / "labeled"
OUTPUT_FILE = PROJECT_ROOT / "data" / "combined" / "combined_cleaned_data.csv"


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    csv_files = sorted(INPUT_DIR.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {INPUT_DIR}")

    dataframes = [pd.read_csv(file) for file in csv_files]
    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df = combined_df.dropna(how="any").drop_duplicates()

    combined_df.to_csv(OUTPUT_FILE, index=False)
    print(f"Merged and cleaned data saved to: {OUTPUT_FILE} ({len(combined_df)} rows)")


if __name__ == "__main__":
    main()
