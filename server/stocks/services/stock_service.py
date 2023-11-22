from stocks.repository.stock_repository import StockRepository

class StockService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StockService, cls).__new__(cls)

        return cls._instance
    
    def GetStocks(self):
        repo = StockRepository()
        return repo.GetStocks()