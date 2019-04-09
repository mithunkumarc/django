#### agenda : creating table using model
#### using in memory database sqlite


        In Django, a model is a class which is used to contain essential fields and methods. 
        Each model class maps to a single table in the database.

        by default model uses sqlite database

#### creating project

        django-admin startproject model_example

#### create app inside project

        model_example > python3 manage.py startapp student
        
        * if it doesn't works than install     "pip3 install django"


#### install django libraries

        pip3 install django



#### create virtual environment


          virtualenv venv -p python3
          source venv/bin/activate




#### create student model in student app , path : student/models.py


            from django.db import models

            # Create your models here.
            class Student(models.Model):  
                first_name = models.CharField(max_length=20)  
                last_name  = models.CharField(max_length=30)  
                contact    = models.IntegerField()  
                email      = models.EmailField(max_length=50)  
                age        = models.IntegerField()   



#### add python plugin : 

            
            settings > project model_example > interprter > add django

#### register app 

              add "student" app in INSTALLED APP

#### migrate : prepare database

    # create student table
    model_example > python3 manage.py makemigrations student
    # create django config tables
    model_example > python3 manage.py migrate

#### check sqlite in jade to see created tables




