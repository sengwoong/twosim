from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    refresh_count = serializers.IntegerField()

    class Meta:
        model = User
        fields = [
            'username',
            'refresh_count',
        ]
