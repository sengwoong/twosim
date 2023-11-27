from comment_service import CommentService
from sentiments.services.sentiment_service import SentimentService

class SentimentFacade:
    @staticmethod
    def CreateSentiment(comment_id):
        # comment = CommentService().GetComment(id=comment_id)
        # if comment is None:
        #     return False
        
        description = description
        sentiment = SentimentService().CreateSentiment(description=description)
        if sentiment is None:
            return False
        
        return CommentService().ConnectSentiment(comment_id, sentiment=sentiment)


    @staticmethod
    def GetSentimentByCommentID(comment_id):
        comment = CommentService().GetComment(id=comment_id)

        sentiment = comment.sentiment
        return sentiment
    
    @staticmethod
    def GetSentimentByID(id):
        sentiment = SentimentService().GetSentiment(sentiment_id=id)
        return sentiment
    
