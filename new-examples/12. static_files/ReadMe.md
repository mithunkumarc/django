Django Static Files Handling

* In a web application, apart from business logic and data handling, we also need to handle and manage static resources like CSS, JavaScript, images etc.

* It is important to manage these resources so that it does not affect our application performance.

* Django deals with it very efficiently and provides a convenient manner to use resources.

* The django.contrib.staticfiles module helps to manage them.





#### 1. creating project :

        django-admin startproject static_ex


#### 2. creating module/app :

        static_ex > python3 manage.py startapp mytemplate
        
        all remaining command must run under static_ex >

#### 3. enabling virtual env for python :

        virtualenv venv -p python3
        source venv/bin/activate



#### 4. creating static folder under mytemplate app

	      mytemplate/static

#### 5. under static folder save images

          mytemplate/static/someimage.jpg 
          
          : in example django.jpg


#### 6. create javascript files under mytemplate/static/js/script.js

          alert("hello, welcome to django");


#### 7. create css files under mytemplate/static/css/style.css

          h2{
              color:red;
          }


#### 8.template :  mytemplate/template/index.html


          <!DOCTYPE html>
          <html lang="en">
          
          <head>
              <meta charset="UTF-8">
              <title>Index</title>
              <!-- loading static folder -->
              {% load static %}         
              <!-- loading js file -->
              <script src="{% static '/js/script.js' %}" type="text/javascript"></script>
          </head>
          
          <body>
                <h2>Welcome to Django!!!</h2>
                <!-- loading css file -->
                <link href="{% static 'css/style.css' %}" rel="stylesheet">                
                <!-- message from response -->
                <h3>{{ message }}</h3>                
                <img src="{% static '/django.jpg' %}" alt="My image" height="300px" width="700px"/>
          </body>
          </html>




#### 9. mytemplate/views.py

            from django.shortcuts import render
            from django.template import loader
            from django.http import HttpResponse

            def index(request):
                template = loader.get_template('index.html')
                name = {
                        'message':'this is a template example'
                }
                return HttpResponse(template.render(name))	



#### 10. install django libray is missing

        pip3 install django



#### 11. mytemplate/urls.py


        from django.urls import path
        from mytemplate.views import index

        urlpatterns = [    
            path('index/', index, name='home_page')    
        ]

        # * name = 'home page' : check name url at the end 


#### 12 : static_ex/urls.py

         from django.contrib import admin
         from django.urls import include, path

         urlpatterns = [
             path('mytemplate/', include('mytemplate.urls')),
             path('admin/', admin.site.urls),
         ]



#### 13. add mytemplate app in settings
  
          go to settings.py file under static_ex, add 'mytemplate' in INSTALLED_APP


#### 14. add template base dir in template, tell django the path of template


      	 'DIRS': [os.path.join(BASE_DIR,'templates')],


#### 15. prepare db, optional
        
        python3 manage.py migrate  
        
          

#### 16. runserver :

        python3 manage.py runserver

        or

        python3 manage.py runserver <port:number>

#### 17. output : 

        http://127.0.0.1:8000/mytemplate/index/


#### about named url : 

        use name of url instead of hardcoding path in views.py
        
        
        helpful links : 
        https://docs.djangoproject.com/en/2.1/topics/http/urls/#naming-url-patterns
        https://stackoverflow.com/questions/12818377/django-name-parameter-in-urlpatterns




It is just that django gives you the option to name your views in case you need to refer to them from your code, or your templates.
This is useful and good practice because you avoid hardcoding urls on your code or inside your templates. 
Even if you change the actual url, you don't have to change anything else, since you will refer to them by name.

e.x with views:

        from django.http import HttpResponseRedirect
        from django.core.urlresolvers import reverse

        def myview(request):
            passwords_url = reverse('passwords_api_root')  # this returns the string `/passwords/`
            return HttpResponseRedirect(passwords_url)
