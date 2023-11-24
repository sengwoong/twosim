from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

class PageController(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    http_method_names = ['get', 'post']

    def list(self, request):    
        return Response(status=status.HTTP_200_OK, data={}, template_name="index.html")
    
    @action(methods=["get"], detail=False, url_path='login/', url_name="login")
    def login(self, request):
        return Response(status=status.HTTP_200_OK, data={}, template_name="login.html")
    
    @action(methods=["get"], detail=False, url_path='logout/', url_name="logout")
    def logout(self, request):
        return Response(status=status.HTTP_200_OK, data={}, template_name="logout.html")
    
    @action(methods=["get"], detail=False, url_path='join/', url_name="join")
    def join(self, request):
        return Response(status=status.HTTP_200_OK, data={}, template_name="join.html")
    
    @action(methods=["get"], detail=False, url_path='user/', url_name="user")
    def user(self, request):
        return Response(status=status.HTTP_200_OK, data={}, template_name="user.html")

