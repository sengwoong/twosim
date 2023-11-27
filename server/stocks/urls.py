from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .controller.stock_controller import StockController

router = DefaultRouter(trailing_slash=True)
router.register(r'', StockController, basename='stocks')

urlpatterns = [
    path('',  include(router.urls)),
]
