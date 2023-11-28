from stocks.services.stock_service import StockService
from comments.services.crawl_service import CrawlService
from comments.services.comment_service import CommentService

class CommentFacade:
    @staticmethod
    def UpdateComment(stock_code):
        comments = CrawlService().CrawlNaverFinance(stock_code=stock_code)

        for comment in comments:
            CommentFacade.CreateComment(stock_code=stock_code, comment=comment)

        return comments
    
    @staticmethod
    def CreateComment(stock_code, comment):
        stock = StockService().GetStock(code=stock_code)
        if stock is None:
            return False
        
        post_id = comment['post_id']
        title   = comment['title']  
        content = comment['content']
        return CommentService().CreateComment(stock=stock, post_id=post_id, title=title, content=content)
    
    @staticmethod
    def GetCommentList(stock_code):
        stock = StockService().GetStock(code=stock_code)

        if stock is None:
            return None
        
        return CommentService().GetCommentsByStock(stock=stock)

    @staticmethod
    def GetComment(comment_id):
        return CommentService().GetComment(id=comment_id)
    
    @staticmethod
    def DeleteComment(comment_id):
        return CommentService().DeleteComment(id=comment_id)
