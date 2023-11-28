from sentiments.models import Sentiment

class SentimentRepository:
    @staticmethod
    def CreateSentiment(description, sentiment_type):
        sentiment = Sentiment(
            description = description,
        )
        print(sentiment_type)
        if sentiment_type is not None:
            sentiment.sentiment_type = sentiment_type

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