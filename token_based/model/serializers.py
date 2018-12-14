from rest_framework import serializers
from .import models

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Test
        fields = ('id', 'title', 'content', 'author')
