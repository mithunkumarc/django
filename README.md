#### django


### Hello World app

#### 1. check django installation : 
    
     python -m django --version



#### 2. creating project : 
    
     django-admin startproject mysite

#### 3. creating module/app : 
   
     mysite> python manage.py startapp polls


#### 4. enabling virtual env for python :

    virtualenv venv -p python
    
    source venv/bin/activate

#### 5. make changes to below files

#### 5.1 : polls/views.py

      from django.http import HttpResponse

      def index(request):
          return HttpResponse("Hello, world. You're at the polls index.")


#### 5.2 : polls/urls.py

     from django.urls import path

     from . import views

     urlpatterns = [
         path('', views.index, name='index'),
     ]


#### 5.3 : mysite/urls.py

     from django.contrib import admin
     from django.urls import include, path

     urlpatterns = [
         path('polls/', include('polls.urls')),
         path('admin/', admin.site.urls),
     ]



#### 6. install django libray is missing

     pip3 install django



#### 7. runserver : 

    python3 manage.py runserver

    or
    
    python3 manage.py runserver <port:number>



#### source : https://docs.djangoproject.com/en/2.1/intro/tutorial01/
---

#### some important commands

creating project : 
    
     django-admin startproject project_name <br>


starting server : 
    
    python3 manage.py runserver : to start server <br>


starting sub app inside main app: 
    
    python3 manage.py startapp <appname> : 
 
 
views.py    : similar to controller
urls.py     : maps to view
model.py    : db mapping
template.py : html 

