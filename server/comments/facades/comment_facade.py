

from comment_service import CommentService
from crawl_service import CrawlService

class CommentFacade:
    @staticmethod
    def UpdateComment(stock_id):
        comments = CommentService.GetCommentsByStockID(stock_id=stock_id)
        # CrawlService.CrawlNaverFinance()
        return comments