#### django model forms :

        It is a class which is used to create an HTML form by using the Model. 
        It is an efficient way to create a form without writing HTML code.


#### 1.creating project

        django-admin startproject model_form_example


#### 2.create app inside project

        model_form_example > python3 manage.py startapp student


#### 3.install django libraries

        pip3 install django


#### 4.add django package to pycharm plugin

        settings > project > interprter > add django
        
        
#### 5.create virtual environment

        virtualenv venv -p python3
        source venv/bin/activate

#### 6.student/models.py

          from __future__ import unicode_literals
          from django.db import models

          class Student(models.Model):
              first_name = models.CharField(max_length=20)
              last_name  = models.CharField(max_length=30)
              class Meta:
                db_table = "student"  


#### 7.student/form.py

            from django import forms
            from .models import Student  #.models : from current package import Student

            class StuForm(forms.ModelForm):
                class Meta:
                    model = Student
                    fields = "__all__"



#### 8.student/views.py


            from django.shortcuts import render
            from .form import StuForm

            def index(request):
                stu = StuForm()
                return render(request,"index.html",{'stu_form':stu})


#### 9.student/urls.py

              from django.urls import path
              from student import views

              urlpatterns = [
                  path('index/', views.index, name='index'),
              ]
              
#### 10. model_form_example/urls.py

              from django.contrib import admin
              from django.urls import path,include
              from student import views
              urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('student/', include('student.urls')),
              ]  

#### 11. student/templates/

          <!DOCTYPE html>
          <html lang="en">
          <head>
          <meta charset="UTF-8">
          <title>Index</title>
          </head>
          <body>
          <form method="POST" class="post-form">
              {% csrf_token %}
              {{ stu_form.as_p }}
              <button type="submit" class="save btn btn-default">Save</button>
          </form>
          </body>
          </html>


#### 12 student app in settings file, INSTALLED Apps


#### 13 add template directory

        'DIRS': [os.path.join(BASE_DIR,'templates')], in templates
  
  
#### 14 prepare database :

	             python3 manage.py makemigrations student       # student : table
               python3 manage.py migrate                      # django config tables 
             
             

#### 15 python3 manage.py runserver

          link : http://127.0.0.1:8000/student/index/             

