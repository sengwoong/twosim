
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IndexPageView, LoginPageView

router = DefaultRouter(trailing_slash=False)
router.register(r'', IndexPageView, basename='index')
router.register(r'login/', LoginPageView, basename='login')

urlpatterns = [
    path('',  include(router.urls))
]
