from comments.models import Comment
from server.comments.repository.comment_repository import CommentRepository


class CommentService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CommentService, cls).__new__(cls)

        return cls._instance

    def GetCommentsByStockID(self, stock_id):
        return CommentRepository.GetCommentsByStockID(stock_id=stock_id)