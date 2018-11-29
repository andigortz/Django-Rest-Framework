from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.HyperlinkedModelSerializer): # (serializers.ModelSerializer)
    owner = serializers.ReadOnlyField(source='owner.user')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html') # new paramater if using hyperlinked

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'created', 'linenos', 'language', 'style', 'owner', 'highlight',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippet = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True) # queryset=Snippet.objects.all()

    class Meta:
        model = User
        fields = ('url','id', 'user', 'snippet')
