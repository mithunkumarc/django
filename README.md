# django


 <h4> useful commands :<h4> <br>
 creating project : django-admin startproject project_name <br>
 python3 manage.py runserver : to start server <br>
 python3 manage.py startapp <appname> : to create a new app, will create list of module including view.py <br>
 touch <appname>/urls.py : creating urls.py module under newly created app, configuer url path, handling function and name to url,
                            include this urls.py in main app urls.py module
  
  


django allows multiple apps in single project, to make easiert to manage
1. create app(similar to sub module, lets say pages)
   under url.py module
   mention path , handling function , and a name for url
    eg :  path('sub', subPageView, name='subPage') 

2.add this into pages.url inside main app url.py
      path('', include('pages.urls')),
      
      
3.create handling function in views.py

def subPageView(request):
    return HttpResponse('hello sub page')
    
    
4.run and localhost:8000/sub will call subPageView function which return some text response
