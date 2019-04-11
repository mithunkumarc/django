from django.urls import path
from student.views import index,create

urlpatterns = [
    path('index/', index, name='index'),
    path('student_create/', create, name='create'),
]
