from comments.models import Comment
class CommentRepository:
    @staticmethod
    def GetCommentsByStockID(self, stock_id):
        """
        특정 주식 종목에 속한 댓글들을 반환하는 메서드

        Args:
            stock_id (int): 주식 종목의 ID

        Returns:
            QuerySet: 주어진 주식 종목에 속한 댓글들의 QuerySet
        """
        comments = Comment.objects.filter(stock_id=stock_id)
        return comments