from os import name
from stocks.models import Stock


class StockRepository:
    @staticmethod
    def GetStocks():
        return Stock.objects.all()
    
    @staticmethod
    def GetStock(code):
        return Stock.objects.get(code=code)
    
    def CreateStock(code, name, price, description):
        stock =Stock(
            code = code,
            name = name,
            price = price,
            description = description,
        )
        stock.save()

        if stock.id is None:
            return False
        
        return True
