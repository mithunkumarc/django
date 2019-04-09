from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'), # 'index' : Name for this url
]

# name = "index" can be used to resolve urls by name in view.py