from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response 
from todos.models import TodoList
from todos.serializers import TodoListSerializer
# Create your views here.

class TodoList(APIView):
	def get_queryset(self): # note : if you use django rest framework another version, this function maybe not working so you can replace with def get(self, request, format=None)
		todos = TodoList.objects.all()
		serializer = TodoListSerializer(todos, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = TodoListSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
	def get_object(self, pk):
		try:
			return TodoList.objects.get(pk=pk)
		except Todo.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		todos = self.get_object(pk)
		serializer = TodoListSerializer(todos)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		todos = self.get_object(pk)
		serializer = TodoListSerializer(todos, data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		todos = self.get_object(pk)
		todos.delete()
		return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)












