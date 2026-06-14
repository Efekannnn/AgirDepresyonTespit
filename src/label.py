"""Attach a binary label to cleaned posts.

Label ``1`` marks suicide/depression-prone content, ``0`` marks
non-prone content. Reads from ``data/cleaned/`` and writes to
``data/labeled/``.
"""
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "data" / "cleaned" / "cleaned_turkaa_posts.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "labeled" / "labeled_cleaned_turkaa_posts.csv"
LABEL = 0


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(INPUT_FILE)
    data["label"] = LABEL
    data.to_csv(OUTPUT_FILE, index=False)
    print(f"Labeled data saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
