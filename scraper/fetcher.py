# scraper/fetcher.py

import cloudscraper
import time

def fetch_html(url, delay=2):
    time.sleep(delay)
    scraper = cloudscraper.create_scraper(browser={'custom': 'Chrome/120.0.0.0'})  # User-Agent 위장
    response = scraper.get(url)
    if response.status_code == 200:
        return response.text
    raise Exception(f"페이지 로딩 실패: {response.status_code}")
