from django.urls import path
from . import views

urlpatterns = [
    path('ssession', views.setsession),
    path('gsession', views.getsession),
]
