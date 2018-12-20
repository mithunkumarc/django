from django.urls import path
from employeeapp import views

urlpatterns = [
    path('emp/', views.emp, name='employee'),
]