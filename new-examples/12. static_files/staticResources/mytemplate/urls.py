from django.urls import path
from mytemplate.views import index

urlpatterns = [    
    path('index/', index, name='home_page')    
]