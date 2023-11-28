from django.urls import path, include
from rest_framework.routers import DefaultRouter

from sentiments.controller.sentiment_controller import SentimentController

router = DefaultRouter(trailing_slash=True)
router.register(r'', SentimentController, basename='sentiments')

urlpatterns = [
    path('',  include(router.urls)),
]
