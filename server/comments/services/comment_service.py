from comments.models import Comment
from comments.repository.comment_repository import CommentRepository


class CommentService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CommentService, cls).__new__(cls)

        return cls._instance

    def GetCommentsByStock(self, stock):
        return CommentRepository.GetCommentsByStock(stock=stock)
    
    def CreateComment(self, stock, post_id, title, content):
        return CommentRepository.CreateComment(stock=stock, post_id=post_id, title=title, content=content)
    
    def GetComment(self, id):
        return CommentRepository().GetComment(id=id)
    
    def ConnectSentiment(self, id, sentiment):
        return CommentRepository().ConnectSentiment(id, sentiment)
    
    def DeleteComment(self, id):
        return CommentRepository().DeleteComment(id=id)