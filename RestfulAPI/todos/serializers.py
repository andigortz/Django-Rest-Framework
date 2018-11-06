from rest_framework import serializers
from todos.models import Todo

class TodoSerializer(serializers.HyperLinkedModelSerializer):
	user = serializers.ReadOnlyField(source = 'user.username')

	class Meta:
		model = Todo
		fields = ('url', 'id', 'created', 'name', 'email')
		extra_kwrgs = {

			'url': {

				'view_name' : 'todos:todo-detail',

			}


		}