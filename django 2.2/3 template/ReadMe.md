#### create project : 

        >> django-admin startproject mysite

#### activate virtual env
    
        >> cd mysite/   
        virtualenv venv -p python3
        source venv/bin/activate


#### create app polls : 

        >> pip3 install django
        >> python3 manage.py startapp polls


#### add django plugin : pycharm : 

      settings >> project mysite >> project interpreter


#### create directory templates inside polls app

        mysite 
            -- polls 
               -- templates
  
#### create index.html file inside templates folder

            index.html

            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Index</title>
            </head>
            <body>
            <h2>Welcome to Django!!!</h2>
            <h3>{{ message }}</h3>
            </body>
            </html>


####  create a function called index() in polls/views.py which returns index.html


              from django.shortcuts import render
              from django.template import loader
              from django.http import HttpResponse


              def index(request):
                  template = loader.get_template('index.html')  # getting our template
                  name = {
                      'message': 'this is a template example'
                  }
                  return HttpResponse(template.render(name))  # rendering the template in HttpResponse



#### polls/urls.py

              from django.urls import path

              from . import views

              urlpatterns = [
                  path('index/', views.index, name='index'), # 'index' : Name for this url
              ]

              # name = "index" can be used to resolve urls by name in view.py


#### project level(mysite) urls.py add below line

            from django.contrib import admin
            from django.urls import include, path

            urlpatterns = [
                path('polls/', include('polls.urls')),  # included urls of polls
                path('admin/', admin.site.urls),
            ]


#### add 'polls' app in installed apps , settings.py


#### add location of templates folder in settings.py module , TEMPLATES.DIR


          'DIRS': [os.path.join(BASE_DIR,'templates')],


#### python3 manage.py migrate


#### python3 manage.py runserver


#### link : http://127.0.0.1:8000/polls/index/
