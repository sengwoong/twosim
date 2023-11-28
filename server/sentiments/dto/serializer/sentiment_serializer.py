from rest_framework import serializers
from sentiments.models import Sentiment


class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment
        fields = [
            'description', 
            'sentiment_type', 
            'status',
        ]
