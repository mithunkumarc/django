from django.urls import path
from . import views

urlpatterns = [
    path('content/', views.content, name='content'),        
]
