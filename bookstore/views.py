from django.shortcuts import render
from rest_framework import generics

from .models import Books, Author, Publisher
from .serializers import BookSerializer, AuthorSerializer, PublisherSerializer

# Create your views here.

# For Listing and Creating = LC
# For Retrieving, Updating and Deleting = RUD

# For books:
class BookListView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer


# For authors:
class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer 

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# For publishers:
class PublisherListView(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherDetailView(generics.RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
