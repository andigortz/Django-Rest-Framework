from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.user')

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'created', 'updated', 'linenos', 'language', 'style', 'owner')

class UserSerializer(serializers.ModelSerializer):
    snippet = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'user', 'snippet')
