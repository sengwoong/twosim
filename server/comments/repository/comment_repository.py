from turtle import pos
from comments.models import Comment
class CommentRepository:
    @staticmethod
    def GetCommentsByStockID(stock_id):
        """
        특정 주식 종목에 속한 댓글들을 반환하는 메서드

        Args:
            stock_id (int): 주식 종목의 ID

        Returns:
            QuerySet: 주어진 주식 종목에 속한 댓글들의 QuerySet
        """
        comments = Comment.objects.filter(stock_id=stock_id)
        return comments
    
    @staticmethod
    def CreateComment(stock, post_id, title, content):
        comment =Comment(
            title=title,
            content=content,
            post_id=post_id,
            sentiment=None,
            stock=stock
        )
        comment.save()

        if comment.id is None:
            return False
        
        return True
