from django.urls import path
from studentapp import views
urlpatterns = [
    path('index/', views.index, name='student_form'),
]