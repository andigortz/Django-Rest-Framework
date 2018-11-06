from users.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.serializers import UserSerializer

# Create your views here.

class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializers_class = UserSerializer

	class UserDetail(generics.RetrieveUpdateDestroyAPIView):
		serializers_class = UserSerializer

		def get_queryset(self):
			return User.objects.all().filter(usernmae=self.request.user)