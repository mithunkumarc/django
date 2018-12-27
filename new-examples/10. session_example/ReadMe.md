A session is a mechanism to store information on the server side during the interaction with the web application.

In Django, by default session stores in the database and also allows file-based and cache based sessions. 

It is implemented via a piece of middleware and can be enabled by using the following code.

Put django.contrib.sessions.middleware.SessionMiddleware in MIDDLEWARE and django.contrib.sessions in INSTALLED_APPS of settings.py file.

To set and get the session in views, we can use request.session and can set multiple times too.






#### 1. creating project :

        django-admin startproject session_ex

#### 2. creating module/app :

        session_ex > python3 manage.py startapp student

#### 3. enabling virtual env for python :

        virtualenv venv -p python3
        source venv/bin/activate

#### 4. student/views.py

        from django.shortcuts import render
        from django.http import HttpResponse


        def setsession(request):
            request.session['sname'] = 'rajat'
            request.session['semail'] = 'rajat.jay@gmail.com'
            return HttpResponse("session is set")


        def getsession(request):
            studentname = request.session['sname']
            studentemail = request.session['semail']
            del request.session['sname'] #: use this to delete session
            return HttpResponse(studentname + " " + studentemail)



#### 5. student/urls.py

        from django.urls import path
        from . import views

        urlpatterns = [    
        path('ssession', views.setsession),
        path('gsession', views.getsession),
        ]


#### 6. session_ex/urls.py

      from django.contrib import admin
      from django.urls import include, path

      urlpatterns = [
         path('student/', include('student.urls')),
         path('admin/', admin.site.urls),
      ]


#### 7. install django libray is missing

      pip3 install django


#### 8. add student app in settings


#### 9. allow django to create session table, python3 manage.py migrate

#### 10. runserver :

        python3 manage.py runserver

        or

        python3 manage.py runserver <port:number>

#### 11. output : 

        http://127.0.0.1:8001/student/ssession : session is set
        http://127.0.0.1:8001/student/gsession


	        use del to delete session



