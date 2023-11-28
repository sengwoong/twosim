from comments.services.comment_service import CommentService
from sentiments.services.sentiment_service import SentimentService
from sentiments.services.gpt_service import GPTService
from sentiments.models import Sentiment
class SentimentFacade:
    @staticmethod
    def CreateSentiment(comment_id):
        comment = CommentService().GetComment(id=comment_id)
        if comment is None:
            return None
        
        response = GPTService().Analysis(comment.content)
        if response is None:
            return None

        description = response.get('choices', [])[0].get('message', None).get('content', None)
        if description is None:
            return None
        
        sentiment_type=None
        if "'중립적'" in description:
            sentiment_type = Sentiment.NEUTRAL
        elif "'긍정적'" in description:
            sentiment_type = Sentiment.POSITIVE
        elif "'부정적'" in description:
            sentiment_type = Sentiment.NEGATIVE
        
        sentiment = SentimentService().CreateSentiment(description=description, sentiment_type=sentiment_type)
        if sentiment is None:
            return None
        
        if not CommentService().ConnectSentiment(comment_id, sentiment=sentiment):
            return None

        return sentiment


    @staticmethod
    def GetSentimentByCommentID(comment_id):
        comment = CommentService().GetComment(id=comment_id)

        sentiment = comment.sentiment
        return sentiment
    
    @staticmethod
    def GetSentimentByID(id):
        sentiment = SentimentService().GetSentiment(sentiment_id=id)
        return sentiment
    
