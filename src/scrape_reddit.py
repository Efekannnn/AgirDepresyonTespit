"""Scrape post texts from a subreddit via Reddit's public JSON endpoint.

Output is written to ``data/raw/``.
"""
import time
from pathlib import Path

import httpx
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw"

BASE_URL = "https://www.reddit.com"
SUBREDDIT = "Turkaaaaaaaaaaaaaaaa"
CATEGORY = "top"
PAGES = 10
OUTPUT_FILE = OUTPUT_DIR / "reddit_turkaa_posts.csv"


def scrape_subreddit(subreddit: str, category: str, pages: int) -> list[str]:
    url = f"{BASE_URL}/r/{subreddit}/{category}.json"
    after_post_id = None
    dataset: list[str] = []

    for _ in range(pages):
        params = {"limit": 100, "t": "year", "after": after_post_id}
        response = httpx.get(url, params=params)
        print(f'fetching "{response.url}"...')
        if response.status_code != 200:
            raise RuntimeError(f"Failed to fetch data (status {response.status_code})")

        json_data = response.json()
        dataset.extend(
            rec["data"]["selftext"]
            for rec in json_data["data"]["children"]
            if "selftext" in rec["data"]
        )

        after_post_id = json_data["data"]["after"]
        time.sleep(0.5)

    return dataset


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    dataset = scrape_subreddit(SUBREDDIT, CATEGORY, PAGES)
    pd.DataFrame(dataset, columns=["text"]).to_csv(OUTPUT_FILE, index=False)
    print(f"Saved {len(dataset)} posts to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
