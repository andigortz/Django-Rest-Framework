from django.contrib.auth.models import User
from rest_framework import APIView

# Create your views here.
class UserList(generic.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserDetail(generic.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

