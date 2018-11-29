from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view
from snippet import views

schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [

    url(r'^schema/', schema_view),
    url(r'^snippet/', views.SnippetList.as_view(), name='snippet-list'),
    url(r'^snippet/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    url(r'^snippet/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    url(r'^user/', views.UserList.as_view(), name='user-list'),
    url(r'^user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    url(r'', views.api_root),

]

urlpatterns = format_suffix_patterns(urlpatterns)
