from todos.models import TodoList
from todos.serializers import TodoListSerializer
from rest_framework import mixins
from rest_framework import generics

class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # or use retrieve

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # or use create

    def delete(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # or use destroy
