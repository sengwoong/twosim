from django.test import TestCase

from comments.services.crawl_service import CrawlService

class TestCrawlNaverFinance(TestCase):
    def test_네이버파이낸스_크롤링(self):
        response = CrawlService().CrawlNaverFinance(stock_code='005930')
        print(response)