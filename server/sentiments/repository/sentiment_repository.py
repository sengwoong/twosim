from sentiments.models import Sentiment

class SentimentRepository:
    @staticmethod
    def CreateSentiment(description):
        sentiment = Sentiment(
            description = description
        )
        sentiment.save()

        if sentiment.id is None:
            return None
        
        return sentiment

    @staticmethod
    def GetComment(sentiment):
        comments = sentiment.comment.all()
        return comments
    
    @staticmethod
    def GetSentimentByID(sentiment_id):
        comment = Sentiment.get(id=sentiment_id)
        return comment