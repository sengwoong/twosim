from django.test import TestCase

from server.stocks.services.stock_service import StockService

class TestStocks(TestCase):
    def test_종목_데이터_밀어넣기(self):
        stocks = [
            {
                'code' : '005930', 
                'name' : '삼성전자', 
                'price' : 71700.00, 
                'description' : (
                    "한국 및 DX부문 해외 9개 지역총괄과 DS부문 해외 5개 지역총괄, SDC, Harman 등 230개의 종속기업으로 구성된 글로벌 전자기업임."
                    "세트사업은 TV를 비롯 모니터, 냉장고, 세탁기, 에어컨, 스마트폰, 네트워크시스템, 컴퓨터 등을 생산하는 DX부문이 있음."
                    "부품 사업에는 DRAM, NAND Flash, 모바일AP 등의 제품을 생산하고 있는 DS 부문과 중소형OLED 등의 디스플레이 패널을 생산하고 있는 SDC가 있음."
                )
            },{
                'code' : '005380', 
                'name' : '현대차', 
                'price' : 184000.00, 
                'description' : (
                    "동사는 1967년 12월에 설립되어 1974년 6월 28일에 유가증권시장에 상장됨."
                    "동사는 자동차 및 자동차부품을 제조 및 판매하는 완성차 제조업체로, 현대자동차그룹에 속하였으며, 현대자동차그룹에는 동사를 포함한 국내 53개 계열회사가 있음."
                    "소형 SUV인 코나, 대형 SUV인 팰리세이드, 제네시스 G80 및 GV80 등을 출시하여 SUV 및 고급차 라인업을 강화 하였으며, 수소전기차 넥소를 출시함."
                )
            },
        ]
        for stock in stocks:
            response = StockService().CreateStock(code=stock['code'], name=stock['name'], price=stock['price'], description=stocks['description'])
            print(response)