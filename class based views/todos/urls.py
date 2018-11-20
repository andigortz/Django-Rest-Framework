from django.conf.urls import url
from todos import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

	url(r'^todos/', views.TodoList.as_view()),
	url(r'^todos/<int:pk>/', views.TodoDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)