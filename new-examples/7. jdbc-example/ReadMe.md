#### 1.creating project

        django-admin startproject jdbc_example


#### 2.create app inside project

        jdbc_example > python3 manage.py startapp student


#### 3.install django libraries : run when required

        pip3 install django


#### 4.create virtual environment

        virtualenv venv -p python3
        source venv/bin/activate


#### 5.student/models.py

        from __future__ import unicode_literals  
        from django.db import models  

        class Student(models.Model):  
            first_name = models.CharField(max_length=20)  
            last_name  = models.CharField(max_length=30)  
            class Meta:  
                db_table = "student"



#### 6.student/form.py

        from django import forms  
        from student.models import Student  

        class StuForm(forms.ModelForm):  
            class Meta:  
                model = Student  
                fields = "__all__"


#### 7.student/views.py


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





#### 8.student/urls.py

        from django.urls import path
        from student.views import index,create

        urlpatterns = [
            path('index/', index, name='index'),
            path('student_create/', create, name='create'),
        ] 



#### 9.jdbc_example/urls.py

        from django.contrib import admin
        from django.urls import path,include
        from student import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('student/', include('student.urls')),
        ]


#### 10. student/templates/index.html

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



#### 10. add student app in settings file, INSTALLED Apps


#### 11. add template directory

	    'DIRS': [os.path.join(BASE_DIR,'templates')], in templates


#### 12. add below config into settings.py jdbc 


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


#### 13. downalod mysql connector and client : try all

          : working
          sudo apt-get install python-dev default-libmysqlclient-dev	
	  pip3 install mysqlclient	

	  alternatives : helpful but not working
	  sudo apt-get install python3-dev libmysqlclient-dev	
          sudo apt-get install python-psycopg2 python-mysqldb
          sudo apt-get install libmysqlclient-dev
          sudo pip install MySQL-python
          pip3 install MySQL-python
	  

#### 14. pip3 install django


#### 12. prepare database :

        python3 manage.py makemigrations student
                    python3 manage.py migrate

        check : mysql database

#### 15. python3 manage.py runserver


#### 14. link : http://127.0.0.1:8000/student/index/
