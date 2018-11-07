from todos.models import Todo
from rest_framework import generics
from rest_framework.response import Response 
from rest_framework.reverse impor reverse
from todos.serializers import TodoSerializer


# Create your views here.

class TodoList(generics.ListAPIView):
	queryset = Todo.objects.all()
	serializers_class = TodoSerializer
	
	def list(self, request):
		queryset = self.get_queryset()
		serializer = TodoSerializer(queryset, many=True)
		return Response(serializer.data)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TodoSerializer

	def get_queryset(self):
		return Todo.objects.all().filter(user=self.request.user)



