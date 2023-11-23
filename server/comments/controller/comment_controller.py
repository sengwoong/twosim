from tkinter import NO
from requests import post
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi
from rest_framework.decorators import action
from rest_framework import permissions

from comments.dto.serializer.comment_serializer import CommentSerializer
from comments.facades.comment_facade import CommentFacade

class CommentController(viewsets.ViewSet):
    http_method_names = ['post', 'get']
    
    @swagger_auto_schema(
        operation_description="종토방 댓글을 저장합니다.",
        request_body=CommentSerializer,
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            404: openapi.Response(
                description="종목이 존재하지 않을 때"
            ),
            400: openapi.Response(
                description="파라미터가 정상적이지 않을 때"
            ),
            500: openapi.Response(
                description="Internal Server Error"
            )
        }
    )
    def create(self, request, *args, kwargs):
        data = request.data

        # TO-DO : Change 'get' to 'CommentSerializer'
        stock_code = data.get('stock_code')
        title = data.get('title')
        content = data.get('content')
        post_id = data.get('post_id')
        
        comment = {
            'title' : title,
            'post_id' : post_id,
            'content' : content
        }
        result = CommentFacade.CreateComment(stock_code=stock_code, comment=comment)

        if result is not True:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        
        return Response(status.HTTP_200_OK, data={ "status" : 'created'})
    

    @action(methods=["get"], detail=False, url_path='fetch/(?P<stock_code>\w+)', url_name="fetch", permission_classes=[permissions.IsAdminUser])
    def fetch(self, request, stock_code=None):
        if stock_code is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        
        comments = CommentFacade.UpdateComment(stock_code=stock_code)
        return Response(status=status.HTTP_200_OK, data={'comments':comments}) 
