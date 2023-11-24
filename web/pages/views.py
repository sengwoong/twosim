from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class IndexPageView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def list(self, request):
        context = {}
        return Response(context)
    
class LoginPageView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "login.html"

    def list(self, request):
        context = {}
        return Response(context)
    
class UserPageView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "user.html"

    def list(self, request):
        context = {}
        return Response(context)
    
class LogoutPageView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "logout.html"

    def list(self, request):
        context = {}
        return Response(context)
    
class JoinPageView(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "join.html"

    def list(self, request):
        context = {}
        return Response(context)
    