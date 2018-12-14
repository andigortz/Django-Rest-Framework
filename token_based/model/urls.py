from django.urls import path
from . import views

urlpatterns = [

    path('', views.ListTest.as_view()),
    path('<int:pk>/', views.ListDetail.as_view()),

]
