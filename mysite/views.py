from django.shortcuts import render
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response 

from .models import Books
from .serializers import BookSerializer

# Create your views here.
