from django.db import models
from model_utils.models import StatusModel
from model_utils import Choices

class Sentiment(StatusModel):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    NEUTRAL = 'neutral'

    SENTIMENT_CHOICES = [
        (POSITIVE, '낙관적'),
        (NEGATIVE, '비관적'),
        (NEUTRAL, '중립적'),
    ]

    """
    현재 투자 심리 정보
    
    Attributes:
        description (TextField): 투자 심리에 대한 설명
        sentiment_type (CharField): 투자 심리 상태(낙관적, 비관적, 중립적)
        STATUS (Choices): 초기화 상태
    """
    description = models.TextField()
    sentiment_type = models.CharField(
        max_length=20,
        choices=SENTIMENT_CHOICES,
        default=NEUTRAL,
        verbose_name='투자 심리 상태'
    )
    STATUS = Choices('unspecified', 'specified')

    def __str__(self):
        return f"{self.get_status_display()}-{self.get_sentiment_type_display()}"