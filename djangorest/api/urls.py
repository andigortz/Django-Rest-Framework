from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailView

urlpatterns = [

    url(r'^userlist/$', CreateView.as_view(), name="create"),
    url(r'^userlist/(?P<pk>[0-8]+)/$', DetailView.as_view(), name="detail"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
