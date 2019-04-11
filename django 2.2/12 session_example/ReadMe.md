#### creating project :

          django-admin startproject session_ex

#### creating module/app :

          session_ex > python3 manage.py startapp student


#### enabling virtual env for python :

          virtualenv venv -p python3
          source venv/bin/activate


#### install django library

	        pip3 install django

#### add django plugin to pycahrm

	        file > settings > project > interpreter > add > django


#### student/views.py

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



####  student/urls.py

            from django.urls import path
            from . import views

            urlpatterns = [    
            path('ssession', views.setsession),
            path('gsession', views.getsession),
            ]



####  session_ex/urls.py

            from django.contrib import admin
            from django.urls import include, path

            urlpatterns = [
               path('student/', include('student.urls')),
               path('admin/', admin.site.urls),
            ]




#### add student app in settings.py

            INSTALLED = [
              ...,
              'student'		
            ]


#### mirgration : important to allow django to create sesion table

		        python3 manage.py migrate

		        allow django to create session table, python3 manage.py migrate




#### runserver :

          python3 manage.py runserver



#### output :

        http://127.0.0.1:8001/student/ssession : session is set
        http://127.0.0.1:8001/student/gsession


            use del to delete session

	
