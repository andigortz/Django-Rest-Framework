from rest_framework import generics
from .models import Test
from .serializers import TestSerializer
# Create your views here.
class ListTest(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
