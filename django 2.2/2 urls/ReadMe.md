#### creating project

      Documents >>   django-admin startproject mysite


#### activate virtual env

        >> cd mysite/
        mysite >> virtualenv venv -p python3
        mysite >> source venv/bin/activate
        
        //if you wish to stop virutal env
        deactivate command : deactivate


#### create app inside project 
        
        mysite >> pip3 install django
        mysite >> python3 manage.py startapp polls



#### add django plugin to pycharm 
  
        : settings >> project >> project interpreter >> cick + and search django and install



#### make changes for below files

#### polls/views.py

            from django.shortcuts import render
            # Create your views here.
            from django.http import HttpResponse


            def index(reqimuest):
                return HttpResponse("index link.")


            def contents(reqimuest):
                return HttpResponse("contents link")


#### polls/urls.py : create new file

              from django.urls import path

              from . import views

              urlpatterns = [
                  path('index/', views.index, name='index'), # 'index' : Name for this url
                  path('contents/', views.contents, name='contents'),
              ]

              # name = "index" can be used to resolve urls by name in view.py




#### mysite/urls.py : registering polls/urls.py

              from django.contrib import admin
              from django.urls import include, path

              urlpatterns = [
                  path('polls/', include('polls.urls')),  # included urls of polls
                  path('admin/', admin.site.urls),
              ]


#### python3 manage.py runserver



      http://127.0.0.1:8000/polls/contents/ 
      http://127.0.0.1:8000/polls/index/
      
      ctrl + c : to quit server
