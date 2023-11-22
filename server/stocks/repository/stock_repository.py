from stocks.models import Stock


class StockRepository:
    @staticmethod
    def GetStocks():
        return Stock.objects.all()
    
    @staticmethod
    def GetStock(id):
        return Stock.objects.get(id=id)
