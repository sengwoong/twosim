from users.services.user_service import UserService


class UserFacade:
    @staticmethod
    def GetRefreshCount(user_id):
        return UserService().GetRefreshCount(user_id=user_id)
    
    @staticmethod
    def CanRefresh(user_id):
        count = UserService().GetRefreshCount(user_id=user_id)
        if count > 0 :
            return True
        return False
    
    @staticmethod
    def DecreaseRefreshCount(user_id):
        return UserService().DecreaseRefreshCount(user_id=user_id)
    