#### creating project

        django-admin startproject jdbc_example

#### create app inside project

        cd jdbc_example > 
        python3 manage.py startapp student

#### create virtual environment

        virtualenv venv -p python3
        source venv/bin/activate

#### install django libraries

        pip3 install django

#### add django plugin to pycharm

	      file > settings > project > interpreter > add django

#### student/models.py

        from __future__ import unicode_literals  
        from django.db import models  

        class Student(models.Model):  
            first_name = models.CharField(max_length=20)  
            last_name  = models.CharField(max_length=30)  
            class Meta:  
                db_table = "student"


#### student/form.py

        from django import forms  
        from student.models import Student  

        class StuForm(forms.ModelForm):  
            class Meta:  
                model = Student  
                fields = "__all__"


#### student/views.py

        from django.shortcuts import render,redirect
        from student.form import StuForm
        from django.http import HttpResponse
        from django.views.decorators.http import require_http_methods

        def index(request):
            stu = StuForm()
            return render(request,"index.html",{'form':stu})


        @require_http_methods(["POST"])
        def create(request):
            if request.method == "POST":
                form = StuForm(request.POST)
                if form.is_valid():
                    try:
                        form.save()
                        return redirect('/student/index')
                    except:
                        pass
            else:
                form = StuForm()
            return render(request,'index.html',{'form':form})



#### student/urls.py

            from django.urls import path
            from student.views import index,create

            urlpatterns = [
                path('index/', index, name='index'),
                path('student_create/', create, name='create'),
            ] 



#### jdbc_example/urls.py

            from django.contrib import admin
            from django.urls import path,include
            from student import views
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('student/', include('student.urls')),
            ]



#### student/templates/index.html

            <!DOCTYPE html>  
            <html lang="en">  
            <head>  
            <meta charset="UTF-8">  
            <title>Index</title>  
            </head>  
            <body>  
            <h4>register student name</h4>
            <form method="POST" class="post-form" action="/student/student_create/">  
                {% csrf_token %}  
                {{ form.as_p }}  
                <button type="submit" class="save btn btn-default">Save</button>  
            </form>  
            </body>  
            </html>


#### add student app in settings file, 

            INSTALLED = [
                ...,
                'student'
            ]



#### add template directory


            'DIRS': [os.path.join(BASE_DIR,'templates')], in templates


#### add below config into settings.py jdbc


            DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.mysql',
                        'NAME': 'testjdbc',				#create database testjdbc
                        'USER':'root',
                        'PASSWORD':'root',
                        'HOST':'localhost',
                        'PORT':'3306'
                }
            }



#### downalod mysql connector and client : try all


          sudo apt-get install python-dev default-libmysqlclient-dev	
          pip3 install mysqlclient	




#### prepare database :

              python3 manage.py makemigrations student
              python3 manage.py migrate


#### runserver

              python3 manage.py runserver <port number>
              http://127.0.0.1:8000/student/index/


