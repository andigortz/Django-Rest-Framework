from django.conf.urls import url
from todos import views

urlpatterns = [

	url(r'^todos/', views.todo_list),
	url(r'^todos/<int:pk>/', views.todo_detail),

]