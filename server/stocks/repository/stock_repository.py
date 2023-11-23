from stocks.models import Stock


class StockRepository:
    @staticmethod
    def GetStocks():
        return Stock.objects.all()
    
    @staticmethod
    def GetStock(code):
        return Stock.objects.get(code=code)
