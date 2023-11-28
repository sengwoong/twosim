from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import F

User = get_user_model()

class UserRepository:
    @staticmethod
    @transaction.atomic
    def GetRefreshCount(user_id):
        """
        특정 유저의 RefreshCount 를 조회

        Args:
            user_id (int): 유저의 ID

        Returns:
            QuerySet: 유저의 RefreshCount
        """
        try:
            user = User.objects.get(id=user_id)
            return user.refresh_count
        except Exception as e:
            return None
        
    @staticmethod
    @transaction.atomic
    def DecreaseRefreshCount(user_id):
        return User.objects.filter(id=user_id).update(refresh_count=F('refresh_count') - 1)
    
    @staticmethod
    @transaction.atomic
    def ResetRefreshCount():
        return User.objects.all().update(refresh_count=5)