from todos.models import TodoList
from todos.serializers import TodoListSerializer
from rest_framework import generics

class TodoList(generics.ListCreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

class TodoListSerializer(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
