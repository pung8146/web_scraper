# main.py

from scraper.fetcher import fetch_html
from scraper.parser import extract_post_links, extract_post_data
import pandas as pd

BASE_PAGE = "https://www.example.com/en/vl_genre.php?&mode=&g=aqyq&page={}"
TARGET_PAGES = ['넣고 싶은 페이지']

def main():
    results = []

    for page in TARGET_PAGES:
        list_html = fetch_html(BASE_PAGE.format(page))
        post_links = extract_post_links(list_html)

        for post_url in post_links:
            print(f"처리 중: {post_url}")
            try:
                detail_html = fetch_html(post_url)
                title, links = extract_post_data(detail_html)
                for link in links:
                    results.append({"title": title, "link": link})
            except Exception as e:
                print(f"오류 발생: {e}")

    df = pd.DataFrame(results)
    df.to_csv("data/links.csv", index=False)
    print("완료! links.csv에 저장되었습니다.")

if __name__ == "__main__":
    main()
