#### hello world : 

#### setup

            mitun@mithun-Latitude-E6230:~$ cd Documents/
            mitun@mithun-Latitude-E6230:~/Documents$ cd djangop3/

#### start project with folder structure

            mitun@mithun-Latitude-E6230:~/Documents/djangop3$ django-admin startproject mysite
            mitun@mithun-Latitude-E6230:~/Documents/djangop3$ cd mysite/

#### create app            
            mitun@mithun-Latitude-E6230:~/Documents/djangop3/mysite$ python3 manage.py startapp polls


#### enable virtual env
            
            mitun@mithun-Latitude-E6230:~/Documents/djangop3/mysite$ virtualenv venv -p python3
            mitun@mithun-Latitude-E6230:~/Documents/djangop3/mysite$ source venv/bin/activate
            (venv) mitun@mithun-Latitude-E6230:~/Documents/djangop3/mysite$ 


#### polls/views.py

            from django.http import HttpResponse

            def index(request):
                return HttpResponse("Hello, world. You're at the polls index.")


#### add django package to pycharm
	
            add django package : settings : project : interpreter : add django package
            --or--
            pip3 install django


#### polls/urls.py

           from django.urls import path

           from . import views

           urlpatterns = [
               path('', views.index, name='index'),   # this(empty path) url can be identified as index in views.py
           ]
 

 
           Note :  use name of url instead of hardcoding path in views.py
                   (while redirecting or sending response path), 
                   name can be any unique string to identify particular path


#### mysite/urls.py

           from django.contrib import admin
           from django.urls import include, path

           urlpatterns = [
               path('polls/', include('polls.urls')),
               path('admin/', admin.site.urls),
           ]

#### run project : 

            python3 manage.py runserver

            possible links : 

                    http://127.0.0.1:8001/polls
                    http://127.0.0.1:8001/admin

            http://127.0.0.1:8000/polls/

            response : Hello, world. You're at the polls index.

