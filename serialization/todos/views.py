from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from todos.models import TodoList
from todos.serializers import TodoListSerializer
# Create your views here.

@csrf_exempt
def todo_list(request):

	if request.method == 'GET':
		todos = TodoList.objects.all()
		serializer = TodoListSerializer(todos, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TodoListSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail(request, pk):
	try:
		todos = TodoList.objects.get(pk=pk)
	except TodoList.DoesNotExist:
			return HttpResponse(status=400)

	if request.method == 'GET':
		serializer = TodoListSerializer(todos)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TodoListSerializer(todos, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		todos.delete()
		return HttpResponse(status=204)





