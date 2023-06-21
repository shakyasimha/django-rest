from django.shortcuts import render 
from django.http import Http404
from rest_framework.response import Response 
from rest_framework import status, mixins, generics
from .serializers import SnippetSerializer
from .models import Snippet



# View starts here
"""
    List all snippets, or create a new snippet
"""
class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.APIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



"""
    Retrieve, update, delete
"""
class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.APIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

