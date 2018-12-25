from rest_framework import serializers
from . models import Author, Book, Edition

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author')

class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ('id', 'year', 'book')
