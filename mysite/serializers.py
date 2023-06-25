from rest_framework import serializers 
from .models import Books, Author, Publisher


# Serializer class for authors
class AuthorSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()

    class Meta:
        model  = Author 
        fields = ['author_name', 'nationality', 'date_of_birth']

    def get_author_name(self, obj):
        return f'{obj.last_name}, {obj.first_name}'
    

# Serializer class for Publisher
class PublisherSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField() 

    class Meta:
        model  = Publisher
        fields = ['pub_name', 'address', 'estd']

    def get_address(self, obj):
        return f'{obj.city}, {obj.country}'
    

# Serializer class for Books
class BookSerializer(serializers.ModelSerializer):
    author_name = AuthorSerializer()
    pub_name    = PublisherSerializer()


    class Meta:
        model = Books

        fields = ['id', 'book_name', 'author_name', 'isbn', 'pub_name', 'pub_year']