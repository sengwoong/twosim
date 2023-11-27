from tkinter import NO
from requests import head
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.registration.urls import RegisterView
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes

from users.dto.serializer.user_serializer import UserSerializer

User = get_user_model()

class UserController(viewsets.ViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, required=True, type=openapi.TYPE_STRING),
        ],
        operation_description="유저 정보를 조회합니다.",
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            401: openapi.Response(
                description="인증 정보가 불명확할때"
            ),
            404: openapi.Response(
                description="유저가 존재하지 않을때"
            ),
            500: openapi.Response(
                description="내부 서버 오류"
            )
        }
    )
    @action(methods=["get"], detail=False, url_path='my_info', url_name="my_info")
    def get(self, request, *args, **kwargs):
        headers = request.headers
        if headers is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED, 
                data={'detail': 'UNAUTHORIZED'})
        token = headers.get('Authorization')
        print(token)
        if token is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED, 
                data={'detail': 'UNAUTHORIZED'})

        access_token = AccessToken(token.replace('Bearer ', ''))
        payload = access_token.payload
        user_id = payload['user_id']
        
        # !!! Facade로 변경할 것 !!!
        user = User.objects.get(id=user_id)
        if user is None:
            return Response(status=status.HTTP_404_NOT_FOUND, 
                data={'detail': '유저가 존재하지 않습니다.'})

        if user.is_authenticated == False:
            return Response({'detail': '사용자는 로그아웃된 상태입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        print(user)
        serializer = UserSerializer(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
class CustomTokenBlacklistView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get('refresh_token')
        if refresh_token is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'detail': 'UNAUTHORIZED'})
        
        token = RefreshToken(refresh_token)
        if token is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'detail': 'UNAUTHORIZED'})
        print(type(token))
        token.blacklist()
        return Response(status=status.HTTP_200_OK, data={'detail': 'success'})

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = self.get_response_data(user)

        if data:
            response = Response(
                data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        else:
            response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

        return response
    
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
