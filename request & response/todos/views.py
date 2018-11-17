from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from todos.models import TodoList
from todos.serializers import TodoListSerializer
# Create your views here.

@api_view(['GET', 'PUT'])
def todo_list(request):
	if request.method == 'GET':
		todos = TodoList.objects.all()
		serializer = TodoListSerializer(todos, many=True)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = TodoListSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, serializer.status.HTTP_201_CREATED)
			return Response(serializer.errors, serializer.status.HTTP_400_NOT_OKAY)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
	try:
		todos = TodoList.objects.get(pk=pk)
	except TodoList.DoesNotExist:
		return Respons(serializer.status.HTTP_400_NO_RESPONSE)

		if request.method == 'GET':
			serializer = TodoListSerializer(todos)
			return Response(serializer.data)

		elif request.method == 'PUT':
			serializer = TodoListSerializer(todos, data=data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
				return Response(serializer.errors, serializer.status.HTPP_400_NO_OKAY)

		elif request.method == 'DELETE':
			todos.delete()
			return Response(serializer.status.HTPP_400_NO_CONTENT)












