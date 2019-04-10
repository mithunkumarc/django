# urls.py
from django.urls import path
from .views import MyView

urlpatterns = [
    #path('about/', MyView.as_view()),
    path('about/', MyView.as_view()),
    #path('about/', MyView.as_view(greeting="nice day")),
]
