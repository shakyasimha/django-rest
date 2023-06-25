from rest_framework import serializers 
from .models import Books, Author 


# Serializer class for books
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books 
        fields = ['id', 'book_name', 'author_name', 'isbn']


# Serializer class for authors
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Author 
        fields = ['id', 'author_name', 'date_of_birth']

    