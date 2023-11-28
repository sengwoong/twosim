from sentiments.repository.sentiment_repository import SentimentRepository


class SentimentService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SentimentService, cls).__new__(cls)

        return cls._instance
    
    def CreateSentiment(self, description, sentiment_type):
        return SentimentRepository().CreateSentiment(description=description, sentiment_type=sentiment_type)
    
    def GetSentiment(self, sentiment_id):
        return SentimentRepository().GetSentimentByID(sentiment_id=sentiment_id)
    
    def GetComment(self, sentiment):
        return SentimentRepository().GetComment(sentiment=sentiment)