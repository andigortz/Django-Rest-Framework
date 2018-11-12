from rest_framework import generics
from .models import UserList
from .serializers import UserListSerializer

# Create your views here.
class CreateView(generics.ListCreateAPIView):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer

    def create(self, serializer):
        serializer.save()

class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer
