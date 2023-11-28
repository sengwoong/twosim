from users.repository.user_repository import UserRepository

class UserService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserService, cls).__new__(cls)

        return cls._instance
    
    def GetRefreshCount(self, user_id):
        return UserRepository().GetRefreshCount(user_id=user_id)
    
    def DecreaseRefreshCount(self, user_id):
        return UserRepository().DecreaseRefreshCount(user_id=user_id)