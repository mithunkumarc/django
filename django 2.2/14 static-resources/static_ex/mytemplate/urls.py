from django.urls import path
from .views import index

urlpatterns = [
    path('index/', index, name='home_page')
]

# * name = 'home page' : check name url at the end