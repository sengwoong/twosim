import re
from bs4 import BeautifulSoup
import requests

class CrawlService:
    def CrawlNaverFinance(self, stock_code):
        def GetCommentList(stock_code):
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
                nid_match = re.search(r'nid=(\d+)', link)
                nid = nid_match.group(1) if nid_match else None

                comments.append({
                    'title' : title_element['title'] if title_element else None,
                    'post_id' : nid,
                })

            return comments
        
        def GetContent(stock_code, post_id):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            }
            
            url = f'https://finance.naver.com/item/board_read.naver?code={stock_code}&nid={post_id}'
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                return None

            soup = BeautifulSoup(response.text, 'html.parser')
            body_div = soup.find('div', {'id': 'body'})

            if body_div is None:
                return None
            
            return body_div.get_text().replace('\r','')

        comments = GetCommentList(stock_code=stock_code)
        for comment in comments:
            comment['content'] = GetContent(stock_code=stock_code, post_id=comment['post_id'])

        return comments