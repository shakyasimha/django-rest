from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Snippet




class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet 
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

    owner = serializers.ReadOnlyField(source='owner.username')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'user', 'snippet']