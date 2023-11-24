
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexPageView, JoinPageView, LoginPageView, LogoutPageView, UserPageView

router = DefaultRouter(trailing_slash=False)
router.register(r'', IndexPageView, basename='index')
router.register(r'login/', LoginPageView, basename='login')
router.register(r'user/', UserPageView, basename='user')
router.register(r'logout/', LogoutPageView, basename='logout')
router.register(r'join/', JoinPageView, basename='join')

urlpatterns = [
    path('',  include(router.urls))
]
