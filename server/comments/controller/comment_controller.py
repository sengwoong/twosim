from turtle import st
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from comments.dto.serializer.comment_serializer import CommentDetailSerializer, CommentSerializer
from comments.facades.comment_facade import CommentFacade

class CommentController(viewsets.ViewSet):
    http_method_names = ['post', 'get', 'delete',]
    pagination_class = pagination.PageNumberPagination
    # lookup_field = 'stock_code'
    
    def get_permissions(self):
        # create 메서드에는 IsAuthenticated 권한 적용
        if self.action == 'create':
            return [IsAuthenticated()]
        
        # retrieve 메서드에는 권한 필요 없음
        elif self.action == 'retrieve':
            return [AllowAny()]
        
        # list 메서드에는 권한 필요 없음
        elif self.action == 'list':
            return [AllowAny()]
        
        # delete 메서드는 관리자만 접근 가능
        elif self.action == 'delete':
            return [IsAdminUser()]

        # 기타 경우에는 기본 권한 적용
        else:
            return [IsAuthenticated()]
        
    @swagger_auto_schema(
        operation_description="종토방 댓글을 저장합니다.",
        # request_body=CommentSerializer,
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
    

    @swagger_auto_schema(
        operation_description="종토방 댓글을 불러옵니다.",
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            404: openapi.Response(
                description="종목이 존재하지 않을 때"
            ),
            500: openapi.Response(
                description="Internal Server Error"
            )
        }
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            comment = CommentFacade.GetComment(comment_id=pk)
            serializer = CommentDetailSerializer(comment, many=False)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={})
        
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    @swagger_auto_schema(
        operation_description="종토방 댓글을 불러옵니다.",
        manual_parameters=[
            openapi.Parameter('stock_code', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description='관련 주식 종목 코드'),
        ],
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            404: openapi.Response(
                description="종목이 존재하지 않을 때"
            ),
            500: openapi.Response(
                description="Internal Server Error"
            )
        }
    )
    def list(self, request, *args, **kwargs):
        stock_code = self.request.query_params.get('stock_code', None)
        if stock_code is None:
            return Response(status=status.HTTP_404_NOT_FOUND, data={})
        
        try:
            comments = CommentFacade.GetCommentList(stock_code=stock_code)

            class CustomPagination(pagination.PageNumberPagination):
                page_size = 10
                page_size_query_param = 'page_size'
                max_page_size = 100

            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(comments, request)
            serializer = CommentSerializer(result_page, many=True)
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND, data={})
        
        return paginator.get_paginated_response(serializer.data)

    @swagger_auto_schema(
        operation_description="댓글을 삭제합니다.",
        responses={
            204: openapi.Response(
                description="NO CONTENT"
            ),
            500: openapi.Response(
                description="Internal Server Error"
            )
        }
    )
    def destroy(self, request, pk=None):
        if not CommentFacade().DeleteComment(comment_id=pk):
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={})

        return Response(status=status.HTTP_204_NO_CONTENT, data={"detail": "success"})