# from django.shortcuts import render
# from rest_framework import serializers
# from django.contrib.auth import get_user_model
# from rest_framework.views import APIView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework.response import Response
# from rest_framework import status

# User = get_user_model()

# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'

#     def create(self, validated_data):
#         login_id = validated_data.get('login_id')
#         email = validated_data.get('email')
#         password = validated_data.get('password')
#         user = User(
#             login_id=login_id,
#             email=email
#         )
#         user.set_password(password)
#         user.save()
#         return user
    
# class RegisterAPIView(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
            
#             token = TokenObtainPairSerializer.get_token(user)
#             refresh_token = str(token)
#             access_token = str(token.access_token)
#             res = Response(
#                 {
#                     "user": serializer.data,
#                     "message": "register successs",
#                     "token": {
#                         "access": access_token,
#                         "refresh": refresh_token,
#                     },
#                 },
#                 status=status.HTTP_200_OK,
#             )

#             res.set_cookie("access", access_token, httponly=True)
#             res.set_cookie("refresh", refresh_token, httponly=True)
#             return res
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)