from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [

    url(r'^snippet/', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippet/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^user/', views.UserList.as_view(), name='user-list'),
    url(r'^user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    url(r'', views.api_root_point),

]

urlpatterns = format_suffix_patterns(urlpatterns)
