get and post HttpRequest
and 
Response



1.creating project

    django-admin startproject request_types
	    

2.create app inside project

    open in editor : in terminal 
	
    request_types > python3 manage.py startapp student

3.install django libraries : run when required

    pip3 install django

4.create virtual environment

    virtualenv venv -p python3
    source venv/bin/activate


6.student/form.py

    from django import forms  
    class StuForm(forms.Form):  
        firstname = forms.CharField(label="Enter first name",max_length=50)  
        lastname  = forms.CharField(label="Enter last name", max_length = 100)  


7.student/views.py

		from django.shortcuts import render,redirect  
		from student.forms import StuForm  
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
				            print(form.data)  
			          except:  
				            pass  
		    else:  
			      form = StuForm()  
		        return render(request,'index.html',{'form':form})  



8.student/urls.py : changed

    from django.urls import path
    from student.views import index,create

    urlpatterns = [
        path('index/', index, name='index'),
        path('student_create/', create, name='create'),
    ] 


pip3 install django


9.request_types/urls.py

    from django.contrib import admin
    from django.urls import path,include
    from student import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('student/', include('student.urls')),
    ]

10. student/templates/index.html : changed

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

10. add student app in settings file, INSTALLED Apps


11. add template directory

    'DIRS': [os.path.join(BASE_DIR,'templates')], in templates



15. python3 manage.py runserver

14. link : http://127.0.0.1:8000/student/index/

ignore migrations


sending post request : 

http://127.0.0.1:8000/student/index/

see log to read post data





http://127.0.0.1:8000/student/2003/  : specific for 2003

http://127.0.0.1:8000/student/2018/ : any year other than 2003

http://127.0.0.1:8000/student/2003/03/ : year/month 


