from django.urls import path
from student import views

urlpatterns = [
    path('index/', views.index, name='index'),
]