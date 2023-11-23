from requests import post
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi

from comments.dto.serializer.comment_serializer import CommentSerializer
from comments.facades.comment_facade import CommentFacade

class CommentController(viewsets.ViewSet):
    http_method_names = ['post']
    
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
        stock_id = data.get('stock_id')
        title = data.get('title')
        content = data.get('content')
        post_id = data.get('post_id')
        
        comment = {
            'title' : title,
            'post_id' : post_id,
            'content' : content
        }
        result = CommentFacade.CreateComment(stock_id=stock_id, comment=comment)

        if result is not True:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        
        return Response(status.HTTP_200_OK, data={ "status" : 'created'})
