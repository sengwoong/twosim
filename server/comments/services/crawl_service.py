import re
from bs4 import BeautifulSoup
import requests

class CrawlService:
    def CrawlNaverFinance(self, stock_code):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        
        url = f'https://finance.naver.com/item/board.nhn?code={stock_code}'
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'summary': '종목 토론실의 게시판 글 목록입니다.'})

        if table is None:
            return []
        
        comments = []
        rows = table.select('tbody tr')
        for row in rows:
            title_element = row.select_one('td.title a')
            
            if title_element is None:
                continue

            link = title_element['href'] if title_element else None
            code_match = re.search(r'code=(\d+)', link)
            code = code_match.group(1) if code_match else None

            comments.append({
                'title' : title_element['title'] if title_element else None,
                'post_id' : code,
            })

        return comments