from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import viewsets
from rest_framework.response import Response

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