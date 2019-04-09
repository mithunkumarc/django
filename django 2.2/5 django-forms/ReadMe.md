#### django forms : creates html forms

    Django provides a Form class which is used to create HTML forms. 
    It describes a form and how it works and appears.

    It is similar to the ModelForm class that creates a form by using the Model, 
    but it does not require the Model.
    

####  creating project :

        django-admin startproject django_forms

#### creating app

        cd django_forms
        django_forms >> python3 manage.py startapp student


#### enabling virtual env for python :

            virtualenv venv -p python3
            source venv/bin/activate


#### add django lib

        pip3 install django

#### add django plugin to pycharm

	        settings : project django_forms : interpreter : add django plugin


#### student/forms.py : create module forms.py in student app

          from django import forms  
          class StudentForm(forms.Form):  
              firstname = forms.CharField(label="Enter first name",max_length=50)  
              lastname  = forms.CharField(label="Enter last name", max_length = 100)  



#### student/views.py : handle request


            from django.shortcuts import render
            from .forms import StudentForm

            def index(request):
                student = StudentForm()
                return render(request,"index.html",{'stu_form':student})   # stu_form : key for student html form



#### student/templates/index.html : create template folder

            <!DOCTYPE html>  
            <html lang="en">  
            <head>  
                <meta charset="UTF-8">  
                <title>Index</title>  
            </head>  
            <body>  
            <form method="POST" class="post-form">  
                    {% csrf_token %}  
                    {{ stu_form.as_p }}                    #{{ .as_p }} will render them wrapped in <p> tags
                    
                    <button type="submit" class="save btn btn-default">Save</button>  
            </form>  
            </body>  
            </html>  



#### student/urls.py

           from django.urls import path

           from . import views

           urlpatterns = [
                path('index/', views.index, name='index'),
           ]



#### django_forms/urls.py : add student.urls.py in project level urls.py


            from django.contrib import admin
            from django.urls import include, path

            urlpatterns = [ 
             path('student/', include('student.urls')),       # for students app
             path('admin/', admin.site.urls),
            ]


#### add app in settings.py


            installed = [
                          ..
                        "student"
                        ]


##### add template folder in 


          'DIRS': [os.path.join(BASE_DIR,'templates')], in templates



