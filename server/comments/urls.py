from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments.controller.comment_controller import CommentController

router = DefaultRouter(trailing_slash=True)
router.register(r'', CommentController, basename='comments')

urlpatterns = [
    path('',  include(router.urls)),
]
