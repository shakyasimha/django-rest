from django.shortcuts import render
from rest_framework import generics

from .models import Books
from .serializers import BookSerializer

# Create your views here.

# For listing and creating -> LC
class BookLCView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

# For retrieving, updating and deleting/destroying -> RUD
class BookRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
