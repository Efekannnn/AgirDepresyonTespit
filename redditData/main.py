import time
import httpx
import pandas as pd

base_url = 'https://www.reddit.com'
endpoint = '/r/Turkaaaaaaaaaaaaaaaa/'
category = '/top'

url = base_url + endpoint + category + ".json"
after_post_id = None

headers = {
    #boş
}
dataset = []
for _ in range(10):
    params = {
        'limit': 100,
        't': 'year',
        'after': after_post_id
    }

    response = httpx.get(url, params=params)
    print(f'fetching "{response.url}"...')
    if response.status_code != 200:
        raise Exception('Failed to fetch data')

    json_data = response.json()

    dataset.extend([rec['data']['selftext'] for rec in json_data['data']['children'] if 'selftext' in rec['data']])

    after_post_id = json_data['data']['after']
    time.sleep(0.5)

df = pd.DataFrame(dataset)
df.to_csv('redditHikayeleri.csv', index=False)