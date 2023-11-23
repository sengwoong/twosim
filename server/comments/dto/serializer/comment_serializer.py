from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    stock_code = serializers.CharField()
    post_id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        fields = [
            'stock_code',
            'post_id',
            'title',
            'content'
        ]