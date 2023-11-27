from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    post_id = serializers.CharField()
    title = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        fields = [
            'stock',
            'post_id',
            'title',
            'content'
        ]

        # title (CharField): 댓글 제목
        # content (CharField): 댓글 내용
        # post_id (BigIntegerField): 종토방 게시글 ID
        # sentiment (OneToOneField): 투자 심리와의 1:1 Relationship
        # stock (ForeignKey): 주식 종목과의 1:M Relationship