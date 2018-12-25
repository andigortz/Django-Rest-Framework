from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BookSerializer, EditionSerializer
from .models import Author, Book, Edition
from rest_framework_extensions.mixins import NestedViewSetMixin

# Create your views here.
class AuthorViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class EditionViewSet(NestedViewSetMixin, ModelViewSet):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
