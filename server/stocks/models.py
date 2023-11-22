from django.db import models
from model_utils.models import TimeStampedModel

class Stock(TimeStampedModel):
    """
    종목 정보
    
    Attributes:
        code (CharField): 종목 코드
        name (CharField): 종목 이름
        price (DecimalField): 현재 주식 가격
        created_at (DateTimeField): 등록 일자
        modified_at (DateTimeField): 수정 일자
        description (TextField): 종목 설명
    """
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    class Meta:
        ordering = ['-modified']