from stocks.facades.stock_facade import StockFacade
from comments.services.crawl_service import CrawlService

class CommentFacade:
    @staticmethod
    def UpdateComment(stock_id):
        comments = CrawlService.CrawlNaverFinance(stock_id)

        for comment in comments:
            CommentFacade.CreateComment(stock_id=stock_id, comment=comment)

        return comments
    
    @staticmethod
    def CreateComment(stock_id, comment):
        stock = StockFacade.GetStock(id=stock_id)
        if stock is None:
            return False
        
        return CommentService.CreateComment()
    
