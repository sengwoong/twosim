from django.urls import (
    path, 
    include,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView, 
    TokenVerifyView,
    TokenBlacklistView,
)
from rest_framework.routers import DefaultRouter

from users.controller.user_controller import CustomTokenBlacklistView, UserController

router = DefaultRouter(trailing_slash=True)
router.register(r'users', UserController, basename='users')

user_url_patterns = [
    # 회원가입
    path('join/', include("dj_rest_auth.registration.urls"), name='join'),
    # 로그인
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # 로그아웃
    path('logout/', CustomTokenBlacklistView.as_view(), name='logout'),
    path('',  include(router.urls)),
]
