from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from drf_yasg  import openapi

User = get_user_model()

class JWTLoginStatusView(APIView):
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    @swagger_auto_schema(
        operation_description="로그인 상태를 체크합니다.",
        responses={
            200: openapi.Response(
                description="정상 응답"
            ),
            401: openapi.Response(
                description="인증되지 않은 사용자"
            ),
            500: openapi.Response(
                description="내부 서버 오류"
            )
        }
    )
    def check_login_status(self, request):
        token = request.headers.get('Authorization', None)
        if not token:
            return Response({'detail': 'JWT 토큰이 전달되지 않았습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        access_token = AccessToken(token)
        payload = access_token.payload
        user_id = payload['user_id']
        
        user = User.objects.get(id=user_id)

        if user.is_authenticated:
            return Response({'detail': '사용자는 로그인된 상태입니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': '사용자는 로그아웃된 상태입니다.'}, status=status.HTTP_401_UNAUTHORIZED)
