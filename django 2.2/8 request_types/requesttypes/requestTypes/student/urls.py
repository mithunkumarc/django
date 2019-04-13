from django.urls import path
from student.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('student_create/', create, name='create'),
    path('student_create_get/', create, name = 'create'),
    path('2003/', special_case_2003, name = 'special_case_2003'),
    path('<int:year>/', year_archive, name = 'year_archive'),
    path('<int:year>/<int:month>/', month_archive, name = 'month_archive'),
    path('message/',message_page,name='message_page'),
]    