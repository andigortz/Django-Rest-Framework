from rest_framework import serializers
from todos.models import TodoList

"""conventional code"""
"""class TodoListSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False, max_length=255)
	code = serializers.CharField(style={'base_template' : 'text.html'})
	linenos = serializers.BooleanField(required=False)"""

class TodoListSerializer(serializers.ModelSerializer):
	class Meta:
		model = TodoList
		fields = ('id', 'title', 'code', 'linenos')

	def create(self, validate_data):
		return TodoList.objects.create(**validate_data)

	def update(self, instance, validate_data):
		instance.title = validate_data.get('title', instance.title)
		instance.code = validate_data.get('code', instance.code)
		lnstance.linenos = validate_data.get('linenos', instance.linenos)
		instance.save()
		return instance