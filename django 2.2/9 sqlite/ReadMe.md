#### to use sqlite no extra config is required

                by default django configured to save data to sqlite
                
                        DATABASES = {
                                    'default': {
                                                        'ENGINE': 'django.db.backends.sqlite3',
                                                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                                                }
                                }

#### creating project : 

        >> django-admin startproject model_sql

#### creating app : 

         >> cd model_sql/
         model_sql>> python3 manage.py startapp detailsapp

#### enable virtual env

        virtualenv venv -p python3
        source venv/bin/activate


#### install django libraries

        pip3 install django

#### add django package to pycharm plugin

        settings > project > interprter > add django


#### detailsapp  : create/edit files

        forms.py
        models.py
        urls.py
        views.py


#### model_sql : edit files

        urls.py



#### add detailsapp in settings.py

          INSTALLED = [
                ...
                'detailsapp'
          ]




#### template files

    creating template folder in detailsapp
    
      display.html      : list
      display0.html      : may be for single details
      userdetails.html   : input




#### add template directory to settings.py


          'DIRS': [os.path.join(BASE_DIR,'templates')], in templates



#### prepare database :

           python3 manage.py makemigrations detailsapp       # detailsapp table
           python3 manage.py migrate				# django tables



#### python3 manage.py runserver


    http://127.0.0.1:8002/
    admin/           
    userdetails/        : input form
    display/            : displays list of details


#### use onlite sqlite to read database
