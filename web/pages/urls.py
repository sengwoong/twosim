
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pages.controller.page_controller import PageController

router = DefaultRouter(trailing_slash=False)
router.register(r'', PageController, basename='')

urlpatterns = [
    path('',  include(router.urls))
]
