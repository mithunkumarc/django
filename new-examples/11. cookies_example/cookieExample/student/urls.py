from django.urls import path
from student.views import setcookie,getcookie

urlpatterns = [    
    path('scookie', setcookie),  
    path('gcookie', getcookie),  
]