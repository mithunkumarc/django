#### 1. creating project :

    django-admin startproject class_based_view


#### 2. creating app :

    class_based_view > python3 manage.py startapp student


#### 3.activate virtual env

    virtualenv venv -p python3
    source venv/bin/activate

#### 4. pip3 install django

#### 5. add django package 

        settings > project > interprter > add django package


#### 6. student/views.py

        from django.http import HttpResponse
        from django.views import View


        class MyView(View):
            def get(self, request):
                # <view logic>
                return HttpResponse('result')


#### 7. student/urls.py

        from django.urls import path
        from .views import MyView

        urlpatterns = [
            path('about/', MyView.as_view()),
        ]

    
#### 8. class_based_view/urls.py

          from django.contrib import admin
          from django.urls import include, path

          urlpatterns = [
            path('student/', include('student.urls')),	
            path('admin/', admin.site.urls),
          ]
          
          
#### 9. runserver :

           python3 manage.py runserver

#### 10. result :

            link : http://127.0.0.1:8000/student/about/


#### cutomise output : 


#### student/views.py, using property of class

            from django.http import HttpResponse
            from django.views import View

            class MyView(View):
                greeting = "Good Day"
                def get(self, request):
                # <view logic>
              return HttpResponse(self.greeting)


#### student/urls.py, override default greeting message

              from django.urls import path
              from student.views import MyView

              urlpatterns = [
                    # try all urls
                    #path('about/', MyView.as_view()),
                    path('about/', MyView.as_view()),
                    #path('about/', MyView.as_view(greeting="nice day")),
              ]  
