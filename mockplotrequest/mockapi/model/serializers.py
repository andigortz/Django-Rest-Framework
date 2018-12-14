from rest_framework import serializers
from .import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ('kind', 'starttime', 'endtime', 'baseline', 'station', 'event_type', 'reflector')
