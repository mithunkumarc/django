#### creating project : 

                C:\djexample>django-admin startproject pages_project

                C:\djexample>cd pages_project

                C:\djexample\pages_project>python manage.py startapp pages

                C:\djexample\pages_project>


                1. create project : django-admin startproject pages_project

                when you create project, it create a project folder and inside it creates an app with same name

                output : + ---- pages_project			   : this is project				
                                + ----- pages_project      : this is app 


                2. create app : pages_project> python manage.py startapp pages 				

                it creates an app inside pages_project project folder, now we have two apps, 1. pages_project and 2. pages

                output : + ---- pages_project			   : this is project				
                                + ----- pages_project      : this is app 
                                + ----- pages              : new created app 





create a project
django-admin startproject projectname 






Project level files

    manage.py: 
    It is a command-line utility which allows us to interact with the project in various ways and also used to manage 
    an application.
    
    __init__.py: It is an empty file that tells to the Python that this directory should be considered as a Python package.
    
    settings.py: This file is used to configure application settings such as database connection, static files linking etc.
    
    urls.py: This file contains the listed URLs of the application. 
    In this file, we can mention the URLs and corresponding actions to perform the task and display the view.
    
    wsgi.py: It is an entry-point for WSGI-compatible web servers to serve Django project.


****************************************************************************************************************

create an app : a project can have any number of app
django-admin startapp appname

# after this you will find list of files generated in app folder

****************************************************************************************************************


to run server :
python3 manage.py runserver

to stop press : ctlr + c

to sync database : python3 manage.py migrate

****************************************************************************************************************

 enable virtual machine

 #creating virtual environment :
 project >> virtualenv venv -p python
 
 #activate virtual environment : 
 project >> source venv/bin/activate


***********************************************************************************************************



