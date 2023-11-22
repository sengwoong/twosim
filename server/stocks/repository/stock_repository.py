from stocks.models import Stock


class StockRepository:
    @staticmethod
    def GetStocks():
        return Stock.objects.all()
