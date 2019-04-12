from django.contrib import admin
from django.urls import include, path

urlpatterns = [
   path('student/', include('student.urls')),
   path('admin/', admin.site.urls),
]
