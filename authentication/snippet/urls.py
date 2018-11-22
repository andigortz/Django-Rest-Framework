
from snippet.serializers import UserSerializer

urlpatterns = [

url(r'^users/', views.UserList.as_view()),
url(r'^users/<int:pk>/', views.UserDetail.as_view()),

]