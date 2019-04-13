from django.urls import path
from . import views

urlpatterns = [
    path('emp', views.emp),
    path('show', views.show),
    path('edit/<int:id>', views.edit),  # using function based view, (another type : class based)
    path('update/<int:id>', views.update),  # id is a parameter for update function in views.py
    path('delete/<int:id>', views.destroy),
]