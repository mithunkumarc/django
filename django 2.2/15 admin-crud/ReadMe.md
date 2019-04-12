Django provides an admin site to allow CRUD (Create Read Update Delete) operations on registered app model.

It is a built-in feature of Django that automatically generates interface for models.

register model in admin.py

---


#### 1.creating project

        django-admin startproject admin_example

#### 2.create app inside project

        admin_example > python3 manage.py startapp employee

#### 3.create virtual environment

        virtualenv venv -p python3
        source venv/bin/activate



#### 4.install django libraries

        pip3 install django


#### 5. add django plugin to pycharm

        file > settings > project > interpreter > add django package



#### 6.employee/models.py

        from django.db import models  
        
        class Employee(models.Model):  
            eid     = models.CharField(max_length=20)  
            ename   = models.CharField(max_length=100)  
            econtact = models.CharField(max_length=15)  
            class Meta:  
                db_table = "employee"  






#### 7. employee/admin.py : register employee model to admin

        from django.contrib import admin  
        from employee.models import Employee  
        admin.site.register(Employee) # register Employee in admin  



#### 8. admin_example/urls.py

        from django.contrib import admin
        from django.urls import path

        urlpatterns = [
            path('admin/', admin.site.urls),	    
        ]  



#### 9. add employee app in settings file, INSTALLED Apps

	      'employee',




#### 10. prepare database :

        python3 manage.py makemigrations employee
        python3 manage.py migrate



#### 11. create admin user

        python3 manage.py createsuperuser

        username : mithun@django.com
        password : lenovo123




#### 12. python3 manage.py runserver

	      enter username and password
        
        output : http://127.0.0.1:8000/admin 


* use jade to see db
