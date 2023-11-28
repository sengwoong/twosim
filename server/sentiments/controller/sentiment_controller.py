from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi


from sentiments.facades.sentiment_facade import SentimentFacade
from sentiments.dto.serializer.sentiment_serializer import SentimentSerializer
from comments.dto.serializer.comment_serializer import CommentIDSerializer
from users.facades.user_facade import UserFacade

class SentimentController(viewsets.ViewSet):
    http_method_names = ['post', 'get']
    lookup_field = 'id'
    # pagination_class = pagination.PageNumberPagination

    def get_permissions(self):
        # create 메서드에는 IsAuthenticated 권한 적용
        if self.action == 'create':
            return [IsAuthenticated()]

        # Debug 용 : create 메서드에 AllowAny 적용
        # if self.action == 'create':
        #     return [AllowAny()]
        
        # retrieve 메서드에는 권한 필요 없음
        elif self.action == 'retrieve':
            return [AllowAny()]

        # 기타 경우에는 기본 권한 적용
        else:
            return [IsAuthenticated()]
    
    @swagger_auto_schema(
        operation_description="투자 심리를 분석합니다. ",
        request_body=CommentIDSerializer,
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            403: openapi.Response(
                description="인자가 정상적이지 않을때"
            ),
            500: openapi.Response(
                description="내부 서버 오류"
            )
        }
    )
    def create(self, request, *args, **kwargs):
        data = request.data
        comment_id = data.get('comment_id')

        user_id = request.user.id

        if not UserFacade().CanRefresh(user_id=user_id):
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})

        if comment_id is None:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        
        sentiment = SentimentFacade().CreateSentiment(comment_id=comment_id)
        print(sentiment)
        if sentiment is None:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={})
        
        UserFacade().DecreaseRefreshCount(user_id=user_id)
        return Response(status=status.HTTP_200_OK, data={"status" : "created"})
    
    @swagger_auto_schema(
        operation_description="개별 투자 심리 정보를 조회합니다.",
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            400: openapi.Response(
                description="인자가 정상적이지 않을때"
            ),
            404: openapi.Response(
                description="주식 종목이 존재하지 않을때"
            ),
            500: openapi.Response(
                description="internal Server Error"
            )
        }
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            id = kwargs.get('id')
            sentiment = SentimentFacade.GetSentimentByID(id=id)
            
            if sentiment is None:
                return Response(status=status.HTTP_404_NOT_FOUND, data={})
            
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={})
        
        serializer = SentimentSerializer(sentiment, many=False)
        return Response(status=status.HTTP_200_OK, data=serializer.data)    
    