from stocks.services.stock_service import StockService

class StockFacade:
    @staticmethod
    def GetStockList():
        return StockService().GetStocks()
    
    def GetStock(id):
        return StockService().GetStock(id=id)