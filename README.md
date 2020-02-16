#### installing virtual env in windows : 

            while installing python , select set path for python
            
            C:\Users\mitchann\Documents\python\django\django-example-channels>python -m venv env
            C:\Users\mitchann\Documents\python\django\django-example-channels>env\Scripts\activate
            (env) C:\Users\mitchann\Documents\python\django\django-example-channels>


#### django setup laterst version : 

            for python3 use pip3
            
            install django :  pip3 install Django

            check version  :  python3 -m django --version
            2.2

            >>> import django
            >>> django.__version__
            '2.2'
            >>> 


#### starting server : use virtual environment

                >> cd Documents/
                >> mkdir djangop3
                >> cd djangop3/
                //create project
                >> django-admin startproject mysite
                //create tables for : uses sqlite
                # enable virtual env
                >> virtualenv venv -p python3
                >> source venv/bin/activate

                
                >> python3 manage.py migrate
                //you may run migrate in another terminal
                >> python3 manage.py runserver 8081

                Starting development server at http://127.0.0.1:8000/

#### install django package for pycharm : 


            File > settings > Project(project name)> Project interpreter > add Django package          


#### django


### Hello World app

#### 1. check django installation : 
    
     python3 -m django --version



#### 2. creating project : 
    
     django-admin startproject mysite

#### 3. creating module/app : 
   
     mysite> python3 manage.py startapp polls


#### 4. enabling virtual env for python :

    virtualenv venv -p python3
    
    source venv/bin/activate

    --or--
    source project_env/bin/activate         # project_env: check your project folder(ends with env)
    
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
     
     Note :  use name of url instead of hardcoding path in views.py(while redirecting or sending response path), 
             name can be any unique string to identify particular path


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




#### output link : 
            
            http://127.0.0.1:8001/polls
            http://127.0.0.1:8001/admin
            
#### set admin username and password

            create db for auth_user/admin
            
                python manage.py migrate
            
            creating super user

                python3 manage.py createsuperuser
                
                //follow instructions
                
> admin site lets you to register models
            
            

#### source : https://docs.djangoproject.com/en/2.1/intro/tutorial01/
---

#### some important points 

csrf_token : Cross Site Request Forgery protection
    
    some unique number through which django identifies user. used in forms.

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


#### if pip not working

            https://stackoverflow.com/questions/39832219/pip-not-working-in-python-installation-in-windows-10
