> Django provides built-in methods to validate form data automatically. 

> Django forms submit only if it contains CSRF tokens. 

> It uses uses a clean and easy approach to validate data.

> The is_valid() method is used to perform validation for each field of the form, it is defined in Django Form class. 

> It returns True if data is valid and place all data into a cleaned_data attribute.

---
#### form validation :  using django models form



#### 1.create project

        django-admin startproject FormValidation


#### 2.create app

        FormValidation > django-admin startapp employeeapp


#### 3.enable virtual environment
	
        virtualenv venv -p python3
        source venv/bin/activate



#### 4.create class Employee in employeeapp/Models.py

            from django.db import models

            # Create your models here.
            class Employee(models.Model):
                eid = models.CharField(max_length=20)
                ename = models.CharField(max_length=100)
                econtact = models.CharField(max_length=15)
                class Meta:
            db_table="employee" #associated database table name


#### 4.1. pip3 install django , restart visual studio if needed then activate virtual env


#### 5.EmployeeForm in employeeapp/forms.py


		from django import forms
		from employeeapp.models import Employee

		class EmployeeForm(forms.ModelForm):
		    class Meta:
			model = Employee
			fields = "__all__"



#### 6.write a method in employeeapp/views.py which return employee form through html

		from django.shortcuts import render,redirect
		from .forms import EmployeeForm

		# Create your views here.
		def emp(request):
		    if request.method == 'POST':
			form = EmployeeForm(request.POST)
			if form.is_valid():
			    try:
				return redirect('/')
			    except:
				pass
		    else:
			form = EmployeeForm()
		return render(request,'index.html',{'form':form})


#### 7.employeeapp/templates/index.html

          <!DOCTYPE html>
          <html lang="en">
          <head>
              <meta charset="UTF-8">
              <title>Index</title>
          </head>
          <body>
          <form method="POST" class="post-form" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit" class="save btn btn-default">Save</button>
          </form>
          </body>
          </html>


#### 8. FormValidation/urls.py

        from django.contrib import admin
        from django.urls import path,include
        from employeeapp import views

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('employeeapp/', include('employeeapp.urls')),    
        ]


#### 9. employeeapp/urls.py

        from django.urls import path
        from employeeapp import views

        urlpatterns = [
            path('emp/', views.emp, name='employee'),
        ]


#### 10.add templates path in templates	

  	    'DIRS': [os.path.join(BASE_DIR,'templates')], 


#### 11. In settings.py, add employeeapp in INSTALLED APPS 


#### 12.set up database : 
	       
	           python3 manage.py makemigrations employeeapp
             > python3 manage.py migrate


#### 13. python3 manage.py runserver

link : 
http://127.0.0.1:8000/employeeapp/emp/
