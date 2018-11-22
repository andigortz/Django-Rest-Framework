from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
	snippets = Serializers.PrimaryKeyRelatedField(many=True, queryset=snippet.objects.all())
	class Meta:
		model = User
		fields = ('id', 'username', 'snippets')

class SnippetSerializer(serializers.Serializer):
	owner = serializers.ReadOnlyField(source = 'owner.username')
	

