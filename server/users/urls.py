from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import JWTLoginStatusView

user_url_patterns = [
    # 회원가입
    path('join/', include("dj_rest_auth.registration.urls")),
    # 로그인
    path('user/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/check/', JWTLoginStatusView.as_view(), name="token_check"),
]
