from rest_framework import serializers
from .models import UserList

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserList
        fields = ('id', 'name', 'content', 'date_created', 'date_updated')
        read_only_fields = ('date_created', 'date_updated')
