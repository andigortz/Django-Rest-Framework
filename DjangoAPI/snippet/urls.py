from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [

    url(r'^snippet/', views.SnippetList.as_view()),
    url(r'^snippet/<int:pk>/', views.SnippetDetail.as_view()),
    url(r'^user/', views.UserList.as_view()),
    url(r'^user/<int:pk>/', views.UserDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
