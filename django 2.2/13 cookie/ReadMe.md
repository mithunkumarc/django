cookie

A cookie is a small piece of information which is stored in the client browser.

It is used to store user's data in a file permanently (or for the specified time).

Cookie has its expiry date and time and removes automatically when gets expire.

Django provides built-in methods to set and fetch cookie.

The set_cookie() method is used to set a cookie and get() method is used to get the cookie.

The request.COOKIES['key'] array can also be used to get cookie values.

####  creating project :

        django-admin startproject cookie_ex


#### creating module/app :

        cookie_ex> python3 manage.py startapp student


#### enabling virtual env for python :

        virtualenv venv -p python3
        source venv/bin/activate


#### add django library

	        pip3 instasll django
	

#### add django plugin to pycharm

	        file > settings > project > interpreter > add django



#### student/views.py

          from django.shortcuts import render
          from django.http import HttpResponse


          def setcookie(request):
              response = HttpResponse("Cookie Set")
              response.set_cookie('name', 'rajat')
              # response.delete_cookie('name') : run this line to delete value of cookie 'name'
              return response


          def getcookie(request):
              name = request.COOKIES['name']
              return HttpResponse("name @: " + name);



#### session_ex/urls.py

            from django.contrib import admin
            from django.urls import include, path

            urlpatterns = [
               path('student/', include('student.urls')),
               path('admin/', admin.site.urls),
            ]



#### student/urls.py

            from django.urls import path
            from .views import setcookie, getcookie

            urlpatterns = [
                path('scookie', setcookie),
                path('gcookie', getcookie),
            ]



#### add student app in settings

            INSTALLED_APPS = [
                ...
                'student'
            ]


#### allow django to create table 
    
          python3 manage.py migrate


#### runserver :

          python3 manage.py runserver


#### output :

    http://127.0.0.1:8000/student/scookie	: cookie set
    http://127.0.0.1:8000/student/gcookie   : name @: rajat

    check cookie in browser

