from re import T
from django.db import models
from model_utils.models import TimeStampedModel
from sentiments.models import Sentiment
from stocks.models import Stock

class Comment(TimeStampedModel):
    """
    종토방 댓글 정보
    
    Attributes:
        title (CharField): 댓글 제목
        content (CharField): 댓글 내용
        post_id (BigIntegerField): 종토방 게시글 ID
        sentiment (OneToOneField): 투자 심리와의 1:1 Relationship
        stock (ForeignKey): 주식 종목과의 1:M Relationship
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    post_id = models.BigIntegerField(null=True)
    sentiment = models.OneToOneField(Sentiment, on_delete=models.SET_NULL,blank=True, null=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def __str__(self):
        return self.title