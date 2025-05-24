# scraper/parser.py

from bs4 import BeautifulSoup
import re

BASE_URL = "원하는 url 입력력"

def extract_post_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    video_titles = soup.select('div.video > a')
    return [BASE_URL + a['href'] for a in video_titles]

def extract_post_data(html):
    soup = BeautifulSoup(html, 'html.parser')

    # 제목 추출
    title_tag = soup.find('h3')
    title = title_tag.text.strip() if title_tag else "제목 없음"

    # 댓글에서 다운로드 링크 추출
    comments_section = soup.find('div', id='video_comments')
    links = []

    if comments_section:
        comments = comments_section.find_all('div', class_='comment')
        for comment in comments:
            text = comment.get_text()
            urls = re.findall(r'https?://[^\s]+', text)
            for url in urls:
                if any(domain in url for domain in ['원하는 데이터 형식']):
                    links.append(url)

    return title, links
