from django.urls import path
from .views import setcookie, getcookie

urlpatterns = [
    path('scookie', setcookie),
    path('gcookie', getcookie),
]
