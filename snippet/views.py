from django.shortcuts import render 
from django.contrib.auth.models import User
from rest_framework import mixins, generics, views, permissions
from .serializers import SnippetSerializer, UserSerializer
from .models import Snippet



# View starts here
"""
    List all snippets, or create a new snippet
"""
class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin, views.APIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


"""
    Retrieve, update, delete
"""
class SnippetDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, views.APIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset =  User.objects.all()
    serializer_class = UserSerializer 

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

