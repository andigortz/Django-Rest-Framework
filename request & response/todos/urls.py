from django.conf.urls import url
from todos import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

	url(r'^todos/', views.todo_list),
	url(r'^todos/<int:pk>/', views.todo_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)