from rest_framework import serializers

from sentiments.dto.serializer.sentiment_serializer import SentimentSerializer
from stocks.dto.serializer.stock_serializer import StockSerializer

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    post_id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()
    sentiment = SentimentSerializer()

    class Meta:
        fields = [
            'id'
            'sentiment',
            'post_id',
            'title',
            'content'
        ]

class CommentIDSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    # id = serializers.IntegerField() 

    class Meta:
        fields = [
            'id',
        ]

    def to_representation(self, instance):
        return {'comment_id': instance['id']}
    
    def to_internal_value(self, data):
        return {'id' : data['comment_id']}
    
class CommentDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()
    sentiment = SentimentSerializer()
    stock = StockSerializer()

    class Meta:
        fields = [
            'title',
            'content'
            'sentiment',
            'stock',
        ]
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        return response