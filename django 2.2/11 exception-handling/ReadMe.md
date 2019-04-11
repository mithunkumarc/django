#### creating project :

        django-admin startproject exception_ex


#### creating module/app :

        exception_ex > python3 manage.py startapp student


#### enabling virtual env for python :

        exception_ex > virtualenv venv -p python3
        exception_ex > source venv/bin/activate


#### install django library

        pip3 install django

#### django plugin for pycharm

        file > settings > project > interpreter > add django plugin

####  student/views.py

        from django.http import HttpResponse
        from django.core.exceptions import ObjectDoesNotExist

        def index(request):
            print('type', type(request.GET.get('id')))
            if int(request.GET.get('id')) == 100:
                return HttpResponse("student id : 100, name : vinay")
            else:
                # uncomment below line to run with exception
                # raise ObjectDoesNotExist() 
                # below to handles exception

                # comment for first case and uncomment for second case
                try:
                    raise ObjectDoesNotExist()
                except ObjectDoesNotExist:
                    return HttpResponse('student id '+ request.GET.get('id') + " doesn't exist")





#### student/urls.py

            from django.urls import path
            from student.views import index

            urlpatterns = [
                path('index/', index, name='index'),
            ]




#### exception_ex/urls.py

          from django.contrib import admin
          from django.urls import include, path

          urlpatterns = [
             path('student/', include('student.urls')),
             path('admin/', admin.site.urls),
          ]



#### run server

        exception_ex >python3 manage.py runserver


#### links

          no exception : 
          http://127.0.0.1:8000/student/index/?id=100

          with excpception : 
          http://127.0.0.1:8000/student/index/?id=101
