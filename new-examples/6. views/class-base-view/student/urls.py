from django.urls import path
from student.views import MyView

urlpatterns = [
    path('about/', MyView.as_view(greeting="nice day")),
]  