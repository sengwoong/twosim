from stocks.services.stock_service import StockService

class StockFacade:
    @staticmethod
    def GetStockList():
        return StockService().GetStocks()
    
    def GetStock(code):
        return StockService().GetStock(code=code)
    
    def CreateStock(code, name, price, description):
        return StockService().CreateStock(code, name, price, description)